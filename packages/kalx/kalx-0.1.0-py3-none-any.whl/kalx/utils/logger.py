"""
Logging utility for kalX.
"""

import os
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Create logs directory in user's home directory
LOG_DIR = Path.home() / ".kalx" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "kalx.log"
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
LOG_LEVEL = logging.INFO

def get_logger(name: str) -> logging.Logger:
    """
    Get a configured logger instance.
    
    Args:
        name: The name of the logger (usually __name__)
        
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    
    # Only configure handlers once
    if not hasattr(get_logger, 'handler_added'):
        formatter = logging.Formatter(LOG_FORMAT)
        
        # File handler for complete logging
        file_handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=1024*1024,  # 1MB
            backupCount=5
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        
        # Console handler - silent by default
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.CRITICAL)  # Only show critical errors
        logger.addHandler(console_handler)
        
        get_logger.handler_added = True
        
        # Set logger level
        logger.setLevel(LOG_LEVEL)
    
    return logger
