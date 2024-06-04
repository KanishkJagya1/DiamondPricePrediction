import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    # Paths for saving the train, test, and raw data files
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')
    # Configuration for the data split
    test_size: float = 0.30
    random_state: int = 42

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def init_data_ingestion(self):
        logging.info("Data Ingestion has started...")
        # Check if the data file exists before proceeding
        data_file_path = r'C:\Users\kanis\OneDrive\Documents\DiamondPricePrediction\notebook\data\gemstone.csv'
        if not os.path.exists(data_file_path):
            logging.error(f"The specified file {data_file_path} does not exist.")
            raise FileNotFoundError(f"The specified file {data_file_path} does not exist.")
        
        try:
            # Read the data into a pandas DataFrame
            df = pd.read_csv(data_file_path)
            logging.info("Data successfully read into DataFrame.")

            # Ensure target directory exists for the raw data file
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info(f"Raw data saved at {self.ingestion_config.raw_data_path}")

            # Split the data into training and testing sets
            logging.info("Splitting data into train and test sets.")
            train_set, test_set = train_test_split(df, test_size=self.ingestion_config.test_size,
                                                   random_state=self.ingestion_config.random_state)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Data ingestion and split completed successfully.")

        except Exception as e:
            logging.error(f"Exception occurred during data ingestion: {str(e)}")
            raise CustomException(e, sys)

        return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

# Example usage:
if __name__ == "__main__":
    data_ingestion = DataIngestion()
    train_path, test_path = data_ingestion.init_data_ingestion()
    logging.info(f"Training data path: {train_path}")
    logging.info(f"Testing data path: {test_path}")
