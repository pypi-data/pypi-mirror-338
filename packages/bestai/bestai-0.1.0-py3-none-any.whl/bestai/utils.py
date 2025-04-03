"""Utility functions for the bestai package."""

import json
import logging
import os
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


def setup_logging(
    level: int = logging.INFO,
    log_file: Optional[str] = None,
    log_format: Optional[str] = None,
) -> None:
    """
    Set up logging configuration.
    
    Args:
        level: The logging level (default: INFO)
        log_file: Path to the log file (default: None, logs to console only)
        log_format: Custom log format (default: None, uses a standard format)
    """
    log_format = log_format or "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    handlers = []
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format))
    handlers.append(console_handler)
    
    # File handler if specified
    if log_file:
        try:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(logging.Formatter(log_format))
            handlers.append(file_handler)
        except Exception as e:
            logger.error(f"Failed to set up log file: {str(e)}")
    
    # Configure logging
    logging.basicConfig(
        level=level,
        format=log_format,
        handlers=handlers,
    )


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from a JSON file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        The loaded configuration as a dictionary
    """
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load config from {config_path}: {str(e)}")
        raise


def validate_api_keys() -> Dict[str, bool]:
    """
    Validate that API keys are available in the environment.
    
    Returns:
        Dictionary mapping provider names to boolean indicating availability
    """
    keys = {
        "openai": os.environ.get("OPENAI_API_KEY") is not None,
        "anthropic": os.environ.get("ANTHROPIC_API_KEY") is not None,
        "google": os.environ.get("GOOGLE_API_KEY") is not None,
        "mistral": os.environ.get("MISTRAL_API_KEY") is not None,
        "cohere": os.environ.get("COHERE_API_KEY") is not None,
    }
    
    for provider, available in keys.items():
        if not available:
            logger.warning(f"API key for {provider} not found in environment variables")
    
    return keys


def calculate_token_count(text: str) -> int:
    """
    Estimate the number of tokens in a text.
    This is a simple approximation - for production use, use the tokenizer 
    specific to the model being used.
    
    Args:
        text: The text to count tokens for
        
    Returns:
        Estimated token count
    """
    # Simple approximation: average of 4 characters per token for English text
    return len(text) // 4


def summarize_capabilities(available_models: Dict[str, Dict[str, Any]]) -> Dict[str, List[str]]:
    """
    Create a summary of available models and their capabilities.
    
    Args:
        available_models: Dictionary of model configurations
        
    Returns:
        Dictionary mapping model names to lists of capabilities
    """
    capabilities = {}
    
    for model_id, config in available_models.items():
        if "capabilities" in config:
            capabilities[model_id] = config["capabilities"]
        else:
            # Default capabilities if not specified
            capabilities[model_id] = ["text_generation"]
    
    return capabilities 