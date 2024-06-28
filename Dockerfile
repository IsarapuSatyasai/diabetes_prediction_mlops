FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN python '../scripts/model_training.py'

CMD ["python", "flask_app/app.py"]
