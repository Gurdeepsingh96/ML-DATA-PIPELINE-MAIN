import os
from mlproject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlproject.entity.config_entity import DataTransformationConfig

# right now we are doing the train_test_split 
# if the data would be of the categorical part we would be doing the one hot encoding


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # we areonly adding train_test_spliting csv this data is already cleaned up


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        