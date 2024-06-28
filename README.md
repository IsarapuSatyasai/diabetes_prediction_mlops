# Diabetes Prediction Project

## Overview
This project is an end-to-end data science pipeline for predicting diabetes using machine learning. It covers various stages of a typical data science project, including data preprocessing, model training, and deployment as a web service. The project also incorporates modern practices like containerization, orchestration, monitoring, and continuous integration and deployment (CI/CD).

## Prerequisites
- Python 3.8
- Docker
- Kubernetes
- mlflow
- Airflow
- Prometheus
- Grafana
- GitHub Actions

## Setup Instructions

### Step 1: Clone the Repository
Clone the project repository to your local machine.
```bash
git clone https://github.com/your-username/diabetes-prediction.git
cd diabetes-prediction
```
Step 2: Install Python Dependencies
Install the required Python dependencies using pip.

```bash
pip install -r requirements.txt
```
Step 3: Data Preprocessing
Run the data preprocessing script to prepare the dataset.
```bash
python scripts/data_preprocessing.py
```
Step 4: Model Training
Train the machine learning model using the training script.

```bash
python scripts/model_training.py
```
Step 5: Start the Flask App
Navigate to the flask_app directory and run the Flask application.

```bash
cd flask_app
python app.py
```
The Flask app will be running at http://localhost:5000.

Step 6: Docker
Build and run the Docker container for the Flask app.

```bash
docker-compose up --build
```
This will start the Flask app, Prometheus, and Grafana containers.

Step 7: Kubernetes
Apply the Kubernetes deployment and service configurations.

```bash
kubectl apply -f kubernetes_deployment.yaml
```

Step 8: Prometheus and Grafana Setup
Prometheus Configuration
Create a Prometheus configuration file (prometheus/prometheus.yml).

Add Prometheus service to your docker-compose.yml.

Grafana Configuration
Create a Grafana configuration file (grafana/grafana.ini).
Provision the Prometheus data source (datasource.yml).
Provision the Grafana dashboard (dashboard.yml and diabetes_dashboard.json).
Step 9: Running Prometheus and Grafana
Start Prometheus and Grafana using Docker Compose.

```bash
docker-compose up -d
```
Prometheus will be accessible at http://localhost:9090 and Grafana at http://localhost:3000 (default credentials: admin/admin).

Step 10: Configure Grafana Data Source and Dashboard
Grafana should automatically configure the Prometheus data source and the sample dashboard based on the provisioning files.

Step 11: Access MLflow UI
MLflow is used for tracking experiments. You can start the MLflow server and access the UI.

```bash
mlflow ui
The MLflow UI will be running at http://localhost:5000
```

CI/CD Pipeline
The CI/CD pipeline is configured using GitHub Actions. On every push to the main branch, the pipeline will run the data preprocessing and model training scripts.

Accessing the Services
Flask App: http://localhost:5000
Prometheus: http://localhost:9090
Grafana: http://localhost:3000
MLflow UI: http://localhost:5000
Dependencies
Install the required dependencies using:

```bash
pip install -r requirements.txt
```
Author
This project was developed by [Satya Sai Esarapu].
