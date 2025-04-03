# flake8: noqa: E501

import asyncio
import hashlib
import json
import os
import time
from asyncio import Semaphore
from io import BytesIO
from pathlib import Path
from typing import Dict, List, Optional

import fitz  # type: ignore
from loguru import logger
from PIL import Image

from aicapture.cache import FileCache, HashUtils, ImageCache, TwoLayerCache
from aicapture.settings import MAX_CONCURRENT_TASKS, ImageQuality
from aicapture.vision_models import VisionModel, create_default_vision_model

DEFAULT_PROMPT = """
    Extract the document content, following these guidelines:

    Text Content:
    - Extract all text in correct reading order, preserving original formatting and hierarchy
    - Maintain section headers, subheaders, and their relationships
    - Include all numerical values, units, and technical specifications, 
    - DO NOT summarize the content or skip any sections, we need all the details as possible.

    Tables:
    - Convert to markdown format with clear column headers, keep the nested structure as it is.
    - Preserve all numerical values, units, and relationships
    - Include table title/caption and any reference numbers

    Graphs & Charts:
    - Identify the visualization type (line graph, bar chart, scatter plot, etc.)
    - List all axes labels and their units
    - Describe all the insights, trends, or patterns
    - Include details for all annotations, legends, labels, etc.
    - Explain what the visualization is demonstrating

    Diagrams & Schematics:
    - Identify the type of diagram (block diagram, circuit schematic, flowchart, etc.)
    - List all components and their functions
    - Describe all connections and relationships between components
    - Include all labels, values, or specifications
    - Explain purpose and operation of the diagram

    Images:
    - Describe what the image shows
    - Include all measurements, dimensions, or specifications
    - Capture all text, labels, or annotations
    - Explain the purpose or meaning of the image

    Output in markdown format, with all details, do not include introductory phrases or meta-commentary.
    """


class PDFValidationError(Exception):
    """Raised when PDF validation fails."""

    pass


class ImageValidationError(Exception):
    """Raised when image validation fails."""

    pass


class VisionParser:
    """
    A class for extracting content from PDF documents and images using Vision Language Models.
    Supports multiple VLM providers through a pluggable vision model interface.
    Features:
    - Multiple image processing
    - High-quality image support
    - Configurable concurrency
    - Result caching
    - Text extraction for improved accuracy
    - Direct image file processing
    """

    SUPPORTED_IMAGE_FORMATS = {'jpg', 'jpeg', 'png', 'tiff', 'tif', 'webp', 'bmp'}

    # Class variable for global concurrency control
    _semaphore: Semaphore = Semaphore(MAX_CONCURRENT_TASKS)

    def __init__(  # noqa
        self,
        vision_model: Optional[VisionModel] = None,
        cache_dir: Optional[str] = None,
        max_concurrent_tasks: int = MAX_CONCURRENT_TASKS,
        image_quality: str = ImageQuality.DEFAULT,
        invalidate_cache: bool = False,
        invalidate_image_cache: bool = False,
        prompt: str = DEFAULT_PROMPT,
    ):
        """
        Initialize the VisionParser.

        Args:
            vision_model (Optional[VisionModel]): Vision model instance to use.
            If None, creates default model based on environment settings.
            cache_dir (Optional[str]): Directory to store cached results
            max_concurrent_tasks (int): maximum concurrent API calls
            image_quality (str): Image quality setting (low/high)
            invalidate_cache (bool): If True, ignore cache and overwrite with new results
            invalidate_image_cache (bool): If True, ignore image cache and regenerate images
            prompt (str): The instruction prompt to use for content extraction
        """
        self.vision_model = vision_model or create_default_vision_model()
        self.vision_model.image_quality = image_quality
        self._invalidate_cache = invalidate_cache
        self._invalidate_image_cache = invalidate_image_cache
        self.prompt = prompt
        self.dpi = int(os.getenv("VISION_PARSER_DPI", "333"))

        if max_concurrent_tasks is not None:
            self.__class__._semaphore = Semaphore(max_concurrent_tasks)

        # Initialize caches with only local cache by default
        _file_cache = FileCache(cache_dir)
        _image_cache = ImageCache(cache_dir)
        self.cache = TwoLayerCache(
            file_cache=_file_cache, s3_cache=None, invalidate_cache=invalidate_cache  # type: ignore
        )

    @property
    def invalidate_cache(self) -> bool:
        """Get the invalidate_cache value."""
        return self._invalidate_cache

    @invalidate_cache.setter
    def invalidate_cache(self, value: bool) -> None:
        """
        Set the invalidate_cache value and update the cache accordingly.

        Args:
            value (bool): Whether to invalidate the cache
        """
        self._invalidate_cache = value
        if hasattr(self, 'cache'):
            self.cache.invalidate_cache = value

    @property
    def invalidate_image_cache(self) -> bool:
        """Get the invalidate_image_cache value."""
        return self._invalidate_image_cache

    @invalidate_image_cache.setter
    def invalidate_image_cache(self, value: bool) -> None:
        """
        Set the invalidate_image_cache value.

        Args:
            value (bool): Whether to invalidate the image cache
        """
        self._invalidate_image_cache = value

    def _validate_pdf(self, pdf_path: str) -> None:
        """
        Validate that the file has a PDF extension.

        Args:
            pdf_path (str): Path to the PDF file

        Raises:
            PDFValidationError: If the file doesn't have a .pdf extension
        """
        if not str(pdf_path).lower().endswith(".pdf"):
            raise PDFValidationError("File must have a .pdf extension")

    def _extract_text_from_pdf(self, pdf_path: str) -> List[str]:
        """Extract text content from PDF using PyMuPDF."""
        text_extractions = []
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text = page.get_text()
                text_extractions.append(text)
        return text_extractions

    def _make_user_message(self, text_content: str) -> str:
        """Create enhanced user message with text extraction reference."""
        return f"{self.prompt}\n\nFollowing is the text content extracted from the page, use this for reference and improve accuracy:\n<text_content>\n{text_content}\n</text_content>"

    async def process_page_async(
        self,
        image: Image.Image,
        page_number: int,
        text_content: str = "",
    ) -> Dict:
        """Process a single page asynchronously and return structured content."""
        try:
            # Calculate hash for the image
            img_byte_arr = BytesIO()
            image.save(img_byte_arr, format="PNG")
            page_hash = hashlib.sha256(img_byte_arr.getvalue()).hexdigest()

            logger.debug(f"Waiting for semaphore to process page {page_number}")
            # Process with vision model
            async with self.__class__._semaphore:
                logger.debug(
                    f"Acquired semaphore - Started processing page {page_number}"
                )
                enhanced_prompt = self._make_user_message(text_content)

                content = await self.vision_model.aprocess_image(
                    image,
                    prompt=enhanced_prompt,
                )
                logger.debug(
                    f"Completed processing page {page_number} - Releasing semaphore"
                )

            return {
                "page_number": page_number,
                "page_content": content.strip(),
                "page_hash": page_hash,
                "page_objects": [
                    {
                        "md": content.strip(),
                        "has_image": False,  # not used for now
                    }
                ],
            }

        except Exception as e:
            logger.error(f"Error processing page {page_number}: {str(e)}")
            raise

    def save_markdown_output(self, result: Dict, output_dir: str = "tmp/md") -> None:
        """Save the processing result to a Markdown file.

        Args:
            result (Dict): The processing result
            output_dir (str): Directory to save the markdown file
        """
        try:
            # Create output directory if it doesn't exist
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)

            # Get the original filename and create markdown filename
            original_filename = Path(result["file_object"]["file_name"]).stem
            markdown_file = output_path / f"{original_filename}.md"

            with open(markdown_file, "w", encoding="utf-8") as f:
                for page in result["file_object"]["pages"]:
                    f.write(f"\n===== Page: {page['page_number']} =====\n\n")
                    f.write(page["page_content"])
                    f.write("\n\n")

            logger.info(f"Markdown output saved to {markdown_file}")
        except Exception as e:
            logger.error(f"Error saving markdown output: {str(e)}")
            raise

    def _get_partial_cache_path(self, cache_key: str) -> Path:
        """Get the path for partial results cache file."""
        return self.cache.file_cache.cache_dir / f"{cache_key}_partial.json"

    async def _load_partial_results(self, cache_key: str) -> Dict[int, Dict]:
        """Load partial processing results if they exist."""
        cache_path = self._get_partial_cache_path(cache_key)
        try:
            if cache_path.exists():
                with open(cache_path, "r", encoding="utf-8") as f:
                    return {int(k): v for k, v in json.load(f).items()}
        except Exception as e:
            logger.warning(f"Error loading partial results: {str(e)}")
        return {}

    async def _save_partial_results(self, cache_key: str, pages: List[Dict]) -> None:
        """Save partial processing results."""
        cache_path = self._get_partial_cache_path(cache_key)
        try:
            # Convert list of pages to dict with page_number as key
            pages_dict = {page["page_number"]: page for page in pages}

            # Load existing results and update with new pages
            existing_results = await self._load_partial_results(cache_key)
            existing_results.update(pages_dict)

            # Save updated results
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(existing_results, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved partial results to {cache_path}")
        except Exception as e:
            logger.warning(f"Error saving partial results: {str(e)}")

    async def _validate_and_setup(self, pdf_path: str) -> tuple[Path, str]:
        """Validate PDF file and setup initial processing."""
        pdf_file = Path(pdf_path)
        logger.debug(f"Starting to process PDF file: {pdf_file.name}")

        if not pdf_file.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_file}")

        # Validate PDF
        self._validate_pdf(str(pdf_file))

        # Calculate file hash
        file_hash = HashUtils.calculate_file_hash(str(pdf_file))
        logger.debug(f"Calculated file hash: {file_hash}")

        return pdf_file, file_hash

    async def _process_batch(
        self,
        batch: List[Image.Image],
        start_idx: int,
        text_extractions: List[str],
        partial_results: Dict[int, Dict],
    ) -> tuple[List[Dict], int]:
        """Process a batch of pages."""
        tasks = []
        pages = []
        total_words = 0

        for page_number, image in enumerate(batch, start_idx + 1):
            # Skip if page is already processed
            if page_number in partial_results:
                logger.info(f"Using cached result for page {page_number}")
                pages.append(partial_results[page_number])
                total_words += len(partial_results[page_number]["page_content"].split())
                continue

            text_content = text_extractions[page_number - 1] if text_extractions else ""
            task = asyncio.create_task(
                self.process_page_async(image, page_number, text_content)
            )
            tasks.append(task)

        if tasks:
            start_time = time.time()
            batch_results = await asyncio.gather(*tasks)
            duration = time.time() - start_time

            pages.extend(batch_results)
            total_words += sum(
                len(page["page_content"].split()) for page in batch_results
            )
            logger.info(f"Completed batch in {duration:.2f} seconds")

        return pages, total_words

    async def _compile_results(  # noqa
        self,
        pdf_file: Path,
        cache_key: str,
        pages: List[Dict],
        total_words: int,
        total_pages: int,
    ) -> Dict:
        """Compile final results and clean up temporary files."""
        # Sort pages by page number (as integer) to ensure correct order
        pages.sort(key=lambda x: int(x["page_number"]))

        # Clean up partial results file
        partial_cache = self._get_partial_cache_path(cache_key)
        if partial_cache.exists():
            partial_cache.unlink()

        # Prepare final output
        return {
            "file_object": {
                "file_name": pdf_file.name,
                "cache_key": cache_key,
                "total_pages": total_pages,
                "total_words": total_words,
                "file_full_path": str(pdf_file.absolute()),
                "pages": pages,
            }
        }

    async def process_pdf_async(self, pdf_path: str) -> Dict:
        """Process a PDF file asynchronously and return structured content."""

        # Initial validation and setup
        pdf_file, file_hash = await self._validate_and_setup(pdf_path)
        cache_key = HashUtils.get_cache_key(file_hash, self.prompt)

        try:
            # Check cache unless invalidate_cache is True
            cached_result = await self.cache.get(cache_key)
            if cached_result:
                logger.debug("Found cached results - using cached data")
                self.save_markdown_output(cached_result)
                return cached_result
            # Load any partial results
            partial_results = await self._load_partial_results(cache_key)
            logger.info(f"Found {len(partial_results)} cached pages")

            # Extract text content from PDF
            logger.info(f"Extracting text content from PDF: {pdf_file}")
            text_extractions = self._extract_text_from_pdf(str(pdf_file))

            # Convert PDF to images using PyMuPDF
            logger.info(f"Converting PDF to images: {pdf_file}")
            images = []
            with fitz.open(str(pdf_file)) as doc:
                for page in doc:
                    # Get the page as a pixmap with the specified DPI
                    zoom = (
                        self.dpi / 72
                    )  # Convert DPI to zoom factor (72 is the base DPI)
                    matrix = fitz.Matrix(zoom, zoom)
                    pix = page.get_pixmap(matrix=matrix)

                    # Convert pixmap to PIL Image
                    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
                    images.append(img)

            logger.debug(f"PDF converted to {len(images)} images")

            # Cache the images if not invalidating image cache
            # if not self.invalidate_image_cache:
            #     logger.info(f"Caching {len(images)} images for {cache_key}")
            #     await self.image_cache.cache_images(images, cache_key)

            # Process pages in batches
            batch_size = MAX_CONCURRENT_TASKS
            all_pages = []
            total_words = 0

            for i in range(0, len(images), batch_size):
                batch = images[i : i + batch_size]
                pages, words = await self._process_batch(
                    batch, i, text_extractions, partial_results
                )
                all_pages.extend(pages)
                total_words += words
                await self._save_partial_results(cache_key, all_pages)

            # Clean up images
            for image in images:
                image.close()

            # Compile final results
            result = await self._compile_results(
                pdf_file, cache_key, all_pages, total_words, len(images)
            )

            logger.info("Saving results to cache")
            await self.cache.set(cache_key, result)

            # Generate markdown output
            self.save_markdown_output(result)

            return result

        except Exception as e:
            logger.error(f"Error processing PDF {pdf_file}: {str(e)}")
            raise

    def process_pdf(self, pdf_path: str) -> Dict:
        """
        Synchronous wrapper for process_pdf_async.

        Args:
            pdf_path (str): Path to the PDF file

        Returns:
            dict: Structured content following the specified schema
        """

        async def _run() -> Dict:
            try:
                return await self.process_pdf_async(pdf_path)
            except Exception as e:
                logger.error(f"Error processing PDF: {e}")
                return {}

        return asyncio.run(_run())

    def save_output(self, result: Dict, output_path: str) -> None:
        """Save the processing result to a JSON file."""
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            logger.info(f"Output saved to {output_path}")
        except Exception as e:
            logger.error(f"Error saving output: {str(e)}")

    def _validate_image(self, image_path: str) -> None:
        """
        Validate that the file has a supported image extension.

        Args:
            image_path (str): Path to the image file

        Raises:
            ImageValidationError: If the file doesn't have a supported image extension
        """
        ext = Path(image_path).suffix.lower().lstrip('.')
        if ext not in self.SUPPORTED_IMAGE_FORMATS:
            raise ImageValidationError(
                f"Unsupported image format: {ext}. Supported formats: {', '.join(self.SUPPORTED_IMAGE_FORMATS)}"
            )

    def _optimize_image(self, image: Image.Image) -> Image.Image:
        """
        Optimize image for processing while preserving quality.

        Args:
            image (Image.Image): Input image

        Returns:
            Image.Image: Optimized image
        """
        # Calculate target size while maintaining aspect ratio
        max_dimension = 2000
        ratio = min(max_dimension / max(image.size), 1.0)
        if ratio < 1.0:
            new_size = tuple(int(dim * ratio) for dim in image.size)
            image = image.resize(new_size, Image.Resampling.LANCZOS)  # type: ignore

        return image

    async def process_image_async(self, image_path: str) -> Dict:
        """Process an image file asynchronously and return structured content.

        Args:
            image_path (str): Path to the image file

        Returns:
            Dict: Structured content following the same schema as PDF processing
        """
        # Initial validation and setup
        image_file = Path(image_path)
        logger.debug(f"Starting to process image file: {image_file.name}")

        if not image_file.exists():
            raise FileNotFoundError(f"Image file not found: {image_file}")

        # Validate image format
        self._validate_image(str(image_file))

        # Calculate file hash
        file_hash = HashUtils.calculate_file_hash(str(image_file))
        cache_key = HashUtils.get_cache_key(file_hash, self.prompt)
        logger.debug(f"Calculated cache key: {cache_key}")

        try:
            # Check cache unless invalidate_cache is True
            cached_result = await self.cache.get(cache_key)
            if cached_result:
                logger.debug("Found cached results - using cached data")
                self.save_markdown_output(cached_result)
                return cached_result

            # Load and optimize image
            with Image.open(image_file) as img:
                # Convert to RGB if necessary
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1])
                    img = background
                elif img.mode not in ('RGB', 'L'):
                    img = img.convert('RGB')

                # Optimize image
                img = self._optimize_image(img)

                # Process the image
                page_result = await self.process_page_async(
                    img,
                    page_number=1,
                    text_content="",  # No text content for direct image processing
                )

            # Compile results
            result = {
                "file_object": {
                    "file_name": image_file.name,
                    "cache_key": cache_key,
                    "total_pages": 1,
                    "total_words": len(page_result["page_content"].split()),
                    "file_full_path": str(image_file.absolute()),
                    "pages": [page_result],
                }
            }

            # Save to cache
            logger.info("Saving results to cache")
            await self.cache.set(cache_key, result)

            # Generate markdown output
            self.save_markdown_output(result)

            return result

        except Exception as e:
            logger.error(f"Error processing image {image_file}: {str(e)}")
            raise

    def process_image(self, image_path: str) -> Dict:
        """
        Synchronous wrapper for process_image_async.

        Args:
            image_path (str): Path to the image file

        Returns:
            dict: Structured content following the same schema as PDF processing
        """

        async def _run() -> Dict:
            try:
                return await self.process_image_async(image_path)
            except Exception as e:
                logger.error(f"Error processing image: {e}")
                return {}

        return asyncio.run(_run())

    async def process_folder_async(self, folder_path: str) -> List[Dict]:
        """Process all PDF and image files in a folder asynchronously."""
        results = []
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            try:
                if file.lower().endswith('.pdf'):
                    result = await self.process_pdf_async(file_path)
                    results.append(result)
                elif any(
                    file.lower().endswith(ext) for ext in self.SUPPORTED_IMAGE_FORMATS
                ):
                    result = await self.process_image_async(file_path)
                    results.append(result)
            except Exception as e:
                logger.error(f"Error processing file {file}: {str(e)}")
                continue
        return results
