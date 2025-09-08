import logging
from logging.handlers import TimedRotatingFileHandler
import os
import sys
from pathlib import Path
from core.config.base import AppSettings

def setup_logging(settings: AppSettings):
    """Sets up logging with console and file handlers."""
    
    # Ensure log directory exists
    log_dir = Path(settings.log_path)
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Define log filename
    log_file = log_dir / "rag_chatbot.log"
    
    # Log formatting
    log_formatter = logging.Formatter(
        settings.log_format,
        datefmt=settings.log_date_format
    )
    
    # Get root logger
    logger = logging.getLogger()
    
    # Clear any existing handlers
    logger.handlers.clear()
    
    # Set logging level
    log_level = getattr(logging, settings.log_level.upper(), logging.INFO)
    logger.setLevel(log_level)
    
    # File Handler (rotates based on configuration)
    file_handler = TimedRotatingFileHandler(
        log_file, 
        when=settings.log_rotation, 
        interval=1, 
        backupCount=settings.log_retention
    )
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)
    
    # Console Handler (for real-time logs)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)
    
    # Set specific log levels for noisy libraries
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    
    return logger

def get_logger(name: str):
    """Get a named logger instance."""
    return logging.getLogger(name)