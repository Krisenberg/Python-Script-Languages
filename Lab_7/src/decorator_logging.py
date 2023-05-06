import logging
import time

def log(level):
    log_format = '%(asctime)s - %(levelname)s: %(message)s'
    logging.basicConfig(level=level, format=log_format)