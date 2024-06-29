FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install  -r requirements.txt

COPY . .

EXPOSE 5000

ENV NAME DiabetesPrediction


CMD ["python", "app.py"]