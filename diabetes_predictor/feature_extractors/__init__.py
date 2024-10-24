# diabetes_predictor/feature_extractors/__init__.py

# Importing classes from modules in the feature_extractors package
from .feature_transformer_1 import GenderFeature
from .feature_transformer_1 import EthnicityFeature

# Define the public API for the package
__all__ = [ 'GenderFeature', 'EthnicityFeature']
