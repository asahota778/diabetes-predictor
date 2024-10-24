# diabetes_predictor/preprocessors/drop_na_preprocessor.py
import pandas as pd

class Preprocessor_drop:
    def __init__(self):

        self.columns_to_check = ['age', 'gender', 'ethnicity']

    def remove_nan_rows(self, df):
        # Drop rows with NaN values in the 'age', 'gender', and 'ethnicity' columns
        df_cleaned = df.dropna(subset=self.columns_to_check)
        return df_cleaned