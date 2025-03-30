from flask import Flask, request
from flask_cors import CORS
import shooting_advice_model as shooting_advice_model

app = Flask("shooting-advice-model")
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['POST'])
def run_model():
    data = request.json
    level = data.get('archer_level')
    eye = data.get('archer_eye')
    arrow_locations = data.get('arrow_locations')

    # Convert arrow_locations from objects with x and y keys to a list of floats
    arrow_locations = [[float(arrow['x']), float(arrow['y'])] for arrow in arrow_locations]

    # Pass the processed data to the model
    return shooting_advice_model.run(level, eye, arrow_locations)