"""
This is a generic logger class
"""
import inspect
import logging


def selenium_logger(log_level=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    # Create file handler

    # This wil create a new log for every run
    # file_handler = logging.FileHandler(f"{logger_name}.log", mode="w")
    # #################################################################
    # This will create only log and append after every run
    file_handler = logging.FileHandler(f"selenium_logger.log", mode="a")
    file_handler.setLevel(log_level)

    # create formatter
    formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
                                  datefmt="%m/%d/%Y %I:%M:%S %p")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
