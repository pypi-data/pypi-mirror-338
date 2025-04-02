import logging
import os
from datetime import datetime

def setup_logger():
    logger = logging.getLogger('pasargad')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('pasargad.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()

def log_event(message):
    logger.info(message)