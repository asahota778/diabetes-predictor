# diabetes_predictor/preprocessors/drop_na_preprocessor.py
import pandas as pd

class DropNaPreprocessor:
    def __init__(self, columns_to_check):
        self.columns_to_check = columns_to_check

    def preprocess(self, data: pd.DataFrame):
        return data.dropna(subset=self.columns_to_check)
