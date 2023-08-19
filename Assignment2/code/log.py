import os
import logging.config

def setup_logging():
    log_config_path = os.path.join(os.path.dirname(__file__), "logging.conf")
    logging.config.fileConfig(log_config_path)
    return logging.getLogger("weather_analysis")
