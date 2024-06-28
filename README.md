# Diabetes Prediction Project

## Overview
This project is an end-to-end data science pipeline for predicting diabetes using machine learning. It includes data preprocessing, model training, and deployment as a web service.



## Setup Instructions

### Data Preprocessing
Run the following command to preprocess the data:
python scripts/data_preprocessing.py

### Model Training
Run the following command to train the model:
python scripts/model_training.py

### Flask App
To start the Flask app, navigate to the `flask_app` directory and run:
python app.py

### Docker
Build and run the Docker container:
''
docker-compose up --build
''

### Kubernetes
Apply the Kubernetes deployment and service:
kubectl apply -f kubernetes_deployment.yaml


### Prometheus and Grafana

#### Prometheus Configuration

1. **Prometheus Configuration File (`prometheus/prometheus.yml`)**
   - Create a configuration file for Prometheus.

2. **Prometheus Docker Compose Service**
   - Add a service to your `docker-compose.yml` for Prometheus.

#### Grafana Configuration

1. **Grafana Configuration File (`grafana.ini`)**
   - Create a configuration file for Grafana.

2. **Grafana Data Source Provisioning (`datasource.yml`)**
   - Create a new file `datasource.yml` inside the `grafana/provisioning/datasources` directory to provision the Prometheus data source.

3. **Grafana Dashboard Provisioning (`dashboard.yml`)**
   - Create a new file `dashboard.yml` inside the `grafana/provisioning/dashboards` directory to provision the dashboard.

4. **Grafana Dashboard JSON**
   - Create a sample dashboard JSON configuration file inside the `grafana/provisioning/dashboards` directory.

### Running Prometheus and Grafana

1. **Start Prometheus and Grafana**
   - Navigate to the root of your project directory and run `docker-compose up -d`.

2. **Access Prometheus**
   - Prometheus will be running on `http://localhost:9090`.

3. **Access Grafana**
   - Grafana will be running on `http://localhost:3000`. Log in with the default credentials (`admin/admin`).

4. **Configure Grafana Data Source and Dashboard**
   - Grafana should automatically configure the Prometheus data source and the sample dashboard based on the provisioning files provided.

### CI/CD Pipeline
The CI/CD pipeline is configured using GitHub Actions. On every push to the `main` branch, the pipeline will run the data preprocessing and model training scripts.

## Requirements
- Python 3.8
- Docker
- Kubernetes
- Airflow
- Prometheus
- Grafana
- GitHub Actions

## Dependencies
Install the required dependencies using:
pip install -r requirements.txt

## Author
This project was developed by [Satya Sai Esarapu].
