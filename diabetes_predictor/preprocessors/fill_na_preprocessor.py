# diabetes_predictor/preprocessors/fill_na_preprocessor.py
import pandas as pd

class Preprocessor_fill:
    def __init__(self):
        self.columns_to_fill = ['height', 'weight']  # Columns to fill with mean

    def fill_nan_with_mean(self, df):
        # For each column in the columns_to_fill, replace NaN values with the mean
        for column in self.columns_to_fill:
            print(f"Processing column: {column}")

            # Print the column data before processing 
            print(f"Before conversion to numeric: \n{df[column].head()}")

            # Convert the column to numeric 
            df[column] = pd.to_numeric(df[column], errors='coerce')

            # Print the column data after conversion to numeric 
            print(f"After conversion to numeric: \n{df[column].head()}")

            # Calculate the mean of the column
            mean_value = df[column].mean()
            print(f"Mean of '{column}': {mean_value}")  

            # Fill NaN values with the column mean
            df[column] = df[column].fillna(mean_value)

            # Print the column data after filling NaN values
            print(f"After filling NaN: \n{df[column].head()}")
        
        return df
