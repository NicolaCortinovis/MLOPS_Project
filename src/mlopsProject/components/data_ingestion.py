import os
import urllib.request as request
import zipfile 
from mlopsProject.logging import logger 
from mlopsProject.utils.common import get_size
from mlopsProject.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        """
        Downloads the data from the source url and saves it in the data directory

        Function returns None
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url, 
                filename = self.config.local_data_file
            )
        
            logger.info(f"Downloaded {filename} with following info: \n{headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists of size: {get_size(self.config.local_data_file)}")

    def extract_zip_file(self):
        """
        zip_file_path: str
        
        Extracts the zip file into the data directory
        
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  
    
    def delete_local(self):
        """
        Deletes the local data file

        Function returns None
        """
        os.remove(self.config.local_data_file)
        logger.info(f"Deleted {self.config.local_data_file}")