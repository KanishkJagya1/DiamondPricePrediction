import logging
import os
from datetime import datetime

# Correcting the strftime function to use single quotes inside the double-quoted string
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating the logs directory path
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Creating the full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configuring logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
