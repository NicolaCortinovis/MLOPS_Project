import os
from mlopsProject.logging import logger
from mlopsProject.entity import DataValidationConfig

class DataValidation:
    
    def __init__(self,config: DataValidationConfig):
        self.config = config
    

    def validate_all_files_exists(self) -> bool:
        
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","qag_data"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"Validation status: {validation_status}")
            
            with open(self.config.STATUS_FILE,"r") as f:
                print(f.read())

            return validation_status
        
        except Exception as e:
            raise e