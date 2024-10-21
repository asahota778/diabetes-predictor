# diabetes_predictor/feature_extractors/__init__.py
from abc import ABC, abstractmethod
import pandas as pd

class FeatureExtractor(ABC):
    @abstractmethod
    def transform(self, data: pd.DataFrame):
        pass
