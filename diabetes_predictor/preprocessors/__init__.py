# diabetes_predictor/preprocessors/__init__.py
from .load_data import  DiabetesDataLoader
from .drop_na_preprocessor import Preprocessor_drop
from .fill_na_preprocessor import Preprocessor_fill

__all__ = ['DiabetesDataLoader','Preprocessor_drop', 'Preprocessor_fill']

