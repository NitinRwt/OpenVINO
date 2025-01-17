# app.py
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

# Load the model
model = tf.keras.models.load_model("model.h5")

# Initialize the Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'No input data provided'}), 400
    
    input_data = np.array(data['input']) 
    predictions = model.predict(input_data)
    return jsonify({'predictions': predictions.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
