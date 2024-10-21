# diabetes_predictor/data_loader.py
import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self, test_size=0.2, random_state=42):
        data = pd.read_csv(self.file_path)
        train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
        return train_data, test_data
