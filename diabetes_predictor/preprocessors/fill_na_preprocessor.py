# diabetes_predictor/preprocessors/fill_na_preprocessor.py
import pandas as pd

class FillNaPreprocessor:
    def __init__(self, columns_to_fill):
        self.columns_to_fill = columns_to_fill

    def preprocess(self, data: pd.DataFrame):
        for column in self.columns_to_fill:
            data[column].fillna(data[column].mean(), inplace=True)
        return data
