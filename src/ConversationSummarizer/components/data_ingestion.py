import os
import urllib.request as request # needed to to make HTTP requests
import zipfile
from pathlib import Path
from ConversationSummarizer.logging import logger
from ConversationSummarizer.utils.common import get_size
from ConversationSummarizer.entity import DataIngestionConfig

class DataIngestion:
    # Initialize the DataIngestion class with a configuration object
    def __init__(self, config: DataIngestionConfig):
        self.config = config 
    
    # Define a method for downloading a file
    def download_file(self):
        # Check if the local data file already exists
        if not os.path.exists(self.config.local_data_file):
            # If not, download the file from the source URL and save it to the local data file path
            filename, headers = request.urlretrieve( 
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            # Log the filename and headers of the downloaded file
            logger.info(f"{filename} downloaded with following headers: \n{headers}")
        
        else:
            # If the file already exists, log its size
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        # Define the path where the zip file will be extracted
        unzip_path = self.config.unzip_dir
        
        # Create the unzip directory if it doesn't already exist
        os.makedirs(unzip_path, exist_ok = True)
        
        # Open the local data file as a zip file
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            # Extract all the contents of the zip file to the unzip directory
            zip_ref.extractall(unzip_path)