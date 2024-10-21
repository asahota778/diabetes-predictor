# diabetes_predictor/preprocessors/__init__.py
from .drop_na_preprocessor import DropNaPreprocessor
from .fill_na_preprocessor import FillNaPreprocessor

__all__ = ['DropNaPreprocessor', 'FillNaPreprocessor']

