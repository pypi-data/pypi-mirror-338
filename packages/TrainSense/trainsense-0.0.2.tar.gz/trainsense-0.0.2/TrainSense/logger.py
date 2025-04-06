import logging
import os
import datetime

class TrainLogger:
    def __init__(self, log_file="train.log", level=logging.INFO):
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.logger = logging.getLogger("TrainSenseLogger")
        self.logger.setLevel(level)
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(level)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
    def log_info(self, message: str):
        self.logger.info(f"{message} | {datetime.datetime.now()}")
    def log_warning(self, message: str):
        self.logger.warning(f"{message} | {datetime.datetime.now()}")
    def log_error(self, message: str):
        self.logger.error(f"{message} | {datetime.datetime.now()}")