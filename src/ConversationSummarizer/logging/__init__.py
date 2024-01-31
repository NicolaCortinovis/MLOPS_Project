import os
import sys
import logging 

# Format of the logging message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Path to the logs files
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Creating the directory for the logs if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Setting up the logger
logging.basicConfig(
    level = logging.INFO,   # level of the logger: INFO and above will be logged
    format = logging_str,   # format of the logging message


    # Handlers for the logger:
    handlers = [
        logging.FileHandler(log_filepath), # logging to a file
        logging.StreamHandler(sys.stdout)  # logging to the console
    ]
)

logger = logging.getLogger("ConversationSummarizerLogger")