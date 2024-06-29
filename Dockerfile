FROM python:3.12-slim

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python","scripts/model_training.py","python", "flask_app/app.py"]
