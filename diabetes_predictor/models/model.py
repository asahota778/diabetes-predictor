# diabetes_predictor/models/model.py
from sklearn.linear_model import LogisticRegression

class Model:
    def __init__(self, feature_columns, target_column, **model_hyperparams):

        self.__feature_columns = feature_columns  # Private attribute for feature columns
        self.__target_column = target_column      # Private attribute for target column
        self.__model_hyperparams = model_hyperparams  # Private attribute for model hyperparameters

        # Public attribute for the logistic regression model
        self.model = LogisticRegression(**self.__model_hyperparams)

    def train(self, df):
      
        #Train the model using the provided training data.
        # Extract features (X) and target (y) from the DataFrame
        X_train = df[self.__feature_columns]  # Select the feature columns
        y_train = df[self.__target_column]    # Select the target column

        # Train the logistic regression model
        self.model.fit(X_train, y_train)

    def predict(self, df):

        #Predict the probabilities on new data using the trained model.

        #Parameters:
        # pandas DataFrame containing the data for prediction.
        #Returns:
        #Predicted probabilities for each class.
        
        # Select feature columns for prediction
        X_test = df[self.__feature_columns]
        
        # Return the predicted probabilities
        return self.model.predict_proba(X_test)
