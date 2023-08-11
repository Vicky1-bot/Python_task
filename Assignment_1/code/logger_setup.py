import logging
import datetime

def setup_logger():
    log_filename = f"Weatherlog_{datetime.datetime.now().strftime('%Y-%m-%d')}.log"
    logging.basicConfig(filename=log_filename, level=logging.DEBUG)
    return logging.getLogger(__name__)
