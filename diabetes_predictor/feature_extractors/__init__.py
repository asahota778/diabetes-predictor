# diabetes_predictor/feature_extractors/__init__.py
from .feature_transformer_1 import AgeBinningFeatureExtractor
from .feature_transformer_2 import BMIExtractor

__all__ = ['AgeBinningFeatureExtractor', 'BMIExtractor']
