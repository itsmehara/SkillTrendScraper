# utils.py
import logging

class Logger:
    def __init__(self, log_config):
        logging.basicConfig(
            filename=log_config['file_path'],
            level=getattr(logging, log_config['level'])
        )

    def info(self, message):
        logging.info(message)

# Other utility functions can be added as needed
# ...
