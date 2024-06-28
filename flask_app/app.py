
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open('../flask_app/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    prediction = model.predict([np.array(data)])
    output = prediction[0]
    return render_template('index.html', prediction_text='Diabetes Prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
