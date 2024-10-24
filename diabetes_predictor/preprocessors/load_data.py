import os
import pandas as pd
from sklearn.model_selection import train_test_split

class DiabetesDataLoader:
    def __init__(self, data_dir='data', file_name='sample_diabetes_mellitus_data.csv', test_size=0.4, random_state=32):
        self.file_path = os.path.join(data_dir, file_name)
        self.test_size = test_size
        self.random_state = random_state

    def load_and_split_data(self):
        #Primary method that loads the data and splits it into train and test DataFrames.
        
        # Load the CSV data
        df = pd.read_csv(self.file_path, index_col=0)

        # Split the data into training and testing sets
        train_df, test_df = train_test_split(df, test_size=self.test_size, random_state=self.random_state)

        return train_df, test_df

