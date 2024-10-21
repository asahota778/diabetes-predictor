# diabetes_predictor/feature_extractors/feature_transformer_2.py
import pandas as pd
from . import FeatureExtractor

class BMIExtractor(FeatureExtractor):
    def transform(self, data: pd.DataFrame):
        data['BMI'] = data['weight'] / (data['height']/100) ** 2
        return data
