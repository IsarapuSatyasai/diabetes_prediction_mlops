
import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(input_path, output_path):
    # Load dataset
    data = pd.read_csv(input_path)

    # Handling missing values (if any)
    data.fillna(data.mean(), inplace=True)

    # Splitting data into features and target
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']

    # Splitting data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Save preprocessed data
    preprocessed_data = pd.concat([X_train, y_train], axis=1)
    preprocessed_data.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data('../data/diabetes.csv', '../data/preprocessed_data.csv')