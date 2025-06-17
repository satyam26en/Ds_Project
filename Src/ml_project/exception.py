import sys
import logging

def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: {file_name} at line number: {exc_tb.tb_lineno} with message: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self) -> str:
        return f"CustomException: {self.error_message}"

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:  # Catch the specific exception
        logging.info("Logging has started.")
        raise CustomException(e, sys)  # Pass the exception 'e' and sys module