# diabetes_predictor/models/model.py
from sklearn.ensemble import RandomForestClassifier

class DiabetesModel:
    def __init__(self, feature_columns, target_column, **model_params):
        self.feature_columns = feature_columns
        self.target_column = target_column
        self.model = RandomForestClassifier(**model_params)
    
    def train(self, train_data):
        X_train = train_data[self.feature_columns]
        y_train = train_data[self.target_column]
        self.model.fit(X_train, y_train)
    
    def predict(self, test_data):
        X_test = test_data[self.feature_columns]
        return self.model.predict_proba(X_test)[:, 1]  # return probabilities for the positive class
