from flask import Flask, request
import shooting_advice_model as shooting_advice_model

app = Flask("shooting-advice-model")

@app.route('/', methods=['POST'])
def run_model():
    data = request.json
    level = data.get('archer_level')
    eye = data.get('archer_eye')
    arrow_locations = data.get('arrow_locations')
    return shooting_advice_model.run(level, eye, arrow_locations)
    