
# Flask Backend - Starter Code
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # model prediction logic here
    return jsonify({'risk': 'High'})

if __name__ == '__main__':
    app.run(debug=True)
