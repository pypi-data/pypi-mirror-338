"""
Vision Capture - A powerful Python library for extracting and analyzing content
using Vision Language Models.
"""

from vision_capture.cache import FileCache, ImageCache, TwoLayerCache
from vision_capture.settings import ImageQuality
from vision_capture.vid_capture import VidCapture, VideoConfig, VideoValidationError
from vision_capture.vision_models import (
    AnthropicVisionModel,
    AzureOpenAIVisionModel,
    GeminiVisionModel,
    OpenAIVisionModel,
    VisionModel,
    create_default_vision_model,
)
from vision_capture.vision_parser import VisionParser

__version__ = "0.1.2"
__author__ = "Aitomatic, Inc."
__license__ = "Apache License 2.0"

__all__ = [
    # Main parser
    "VisionParser",
    # Vision models
    "VisionModel",
    "OpenAIVisionModel",
    "GeminiVisionModel",
    "AnthropicVisionModel",
    "AzureOpenAIVisionModel",
    # Settings
    "ImageQuality",
    # Cache utilities
    "FileCache",
    "ImageCache",
    "TwoLayerCache",
    # Video capture
    "VidCapture",
    "VideoConfig",
    "VideoValidationError",
    "create_default_vision_model",
]
