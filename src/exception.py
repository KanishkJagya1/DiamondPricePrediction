import sys
import os

# Add the base directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# Example usage of logging in a try-except block
if __name__ == "__main__":
    try:
        logging.info("Logging has started")
        # Code that raises an exception
        a = 1 / 0
        logging.info("Division performed successfully")
    except Exception as e:
        error_msg = CustomException(e, sys)
        logging.error(error_msg)
        raise  # Re-raise the exception if needed, or handle it as appropriate
