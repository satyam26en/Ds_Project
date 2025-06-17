import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_ml_project.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Remove the duplicate path joining - this line was causing the error
# LOG_FILE = os.path.join(logs_path, LOG_FILE)  # REMOVED THIS LINE

logging.basicConfig(
    filename=logs_path,  # Use logs_path directly
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

if __name__ == "__main__":
    logging.info("Logging has been set up successfully.")
    logging.info(f"Log file created at: {logs_path}")
    logging.info("This is an info message for testing purposes.")
    logging.error("This is an error message for testing purposes.")
    logging.warning("This is a warning message for testing purposes.")
    logging.debug("This is a debug message for testing purposes.")