import os
from mlproject import logger
import pandas as pd
from mlproject.entity.config_entity import DataValidationConfig


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    # this is just one layer validation technique where we are checking weather all columns are present or not 
    # we can do weather the columns which are there having data types same or not as copared to schema.(like float, int)
    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            # checking weather columsn which are there in schema are present in our csv it will add in the .txt file with status
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status, col}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e

