# diabetes_predictor/feature_extractors/feature_transformer_1.py
import pandas as pd
from . import FeatureExtractor

class AgeBinningFeatureExtractor(FeatureExtractor):
    def transform(self, data: pd.DataFrame):
        data['age_binned'] = pd.cut(data['age'], bins=[0, 30, 50, 70, 100], labels=['young', 'middle-aged', 'senior', 'elder'])
        return data
