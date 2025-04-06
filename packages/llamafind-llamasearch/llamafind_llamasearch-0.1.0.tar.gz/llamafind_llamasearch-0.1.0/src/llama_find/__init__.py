"""
LlamaFind Ultimate - Advanced Search Engine with MLX Acceleration

This package provides a powerful search engine framework with built-in ML capabilities,
Elasticsearch integration, and advanced query processing for superior search experiences.
"""

import logging
import os
import sys
from typing import Any, Dict, Optional

__version__ = "1.0.0"

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

logger.info(f"Initializing LlamaFind Ultimate v{__version__}")


# Ensure required directories exist in the package
def ensure_app_dirs():
    """Ensure that necessary application directories exist."""
    # Create config directory if it doesn't exist
    config_dir = os.path.join(os.path.dirname(__file__), "config")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir, exist_ok=True)
        logger.info(f"Created config directory: {config_dir}")

    # Create cache directory if it doesn't exist
    cache_dir = os.path.join(os.path.dirname(__file__), "cache")
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir, exist_ok=True)
        logger.info(f"Created cache directory: {cache_dir}")


# Call ensure_app_dirs if we're not being imported during setup
if not any(arg.endswith("setup.py") for arg in sys.argv):
    ensure_app_dirs()


def get_version() -> str:
    """Return the current version of LlamaFind."""
    return __version__
