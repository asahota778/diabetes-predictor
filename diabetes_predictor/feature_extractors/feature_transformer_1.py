# diabetes_predictor/feature_extractors/feature_transformer_1.py
from abc import ABC, abstractmethod
import pandas as pd

class Feature(ABC):
    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

##Feature transformation 1, geneder to binary

class GenderFeature(Feature):
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        #Encode the 'gender' column where:
        # 1 represents Male
        # 0 represents Female
        df.loc[:, 'gender_encoded'] = df['gender'].apply(lambda x: 1 if x == 'M' else 0)
        return df
    
##Feature transformation 2, categories for ethnicity

class EthnicityFeature(Feature):
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:

        # Define the mapping for ethnicity
        ethnicity_mapping = {
            'Caucasian': 0,
            'Hispanic': 1,
            'African American': 2,
            'Asian': 3,
            'Native American': 4,
            'Other/Unknown': 5
        }
        
        # Apply the mapping, using -1 for NaN values
        df.loc[:, 'ethnicity_encoded'] = df['ethnicity'].map(ethnicity_mapping).fillna(-1).astype(int)
        
        return df
