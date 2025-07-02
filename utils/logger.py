import logging
import os

def setup_logging(log_file='reports/suite.log'):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info("======== Test Session Started ========")

def finish_logging():
    logging.info("======== Test Session Finished ========")
