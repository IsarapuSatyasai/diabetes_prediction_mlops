import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import pickle

def train_model(input_path, model_output_path):
    # Load preprocessed data
    data = pd.read_csv(input_path)

    # Splitting data into features and target
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']

    # Splitting data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # MLflow tracking
    mlflow.set_experiment("Diabetes Prediction")

    with mlflow.start_run():
        # Model training
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Predictions
        y_pred = model.predict(X_test)
        
        # Accuracy
        accuracy = accuracy_score(y_test, y_pred)
        
        # Log metrics
        mlflow.log_metric("accuracy", accuracy)
        
        # Log model
        mlflow.sklearn.log_model(model, "random_forest_model")
        
        # Save model as pickle
        with open(model_output_path, 'wb') as f:
            pickle.dump(model, f)

if __name__ == "__main__":
    train_model('../data/preprocessed_data.csv', '../flask_app/model.pkl')

# Run the following command to start the MLFLOW ui:
import os
os.system('mlflow ui')