from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
import json

app = Flask(__name__)

# Load the model
with open('banglore_home_prices_model.pickle', 'rb') as f:
    model = pickle.load(f)

# Load the column information
with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']

@app.route('/')
def index():
    return render_template('index.html', locations=data_columns[3:])

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        location = request.form['location']
        sqft = float(request.form['sqft'])
        bath = int(request.form['bath'])
        bhk = int(request.form['bhk'])

        loc_index = data_columns.index(location.lower())
        x = np.zeros(len(data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1

        prediction = model.predict([x])[0]
        return render_template('index.html', prediction_text="Estimated Price: {:.2f} Lakhs".format(prediction), locations=data_columns[3:])

    return render_template('index.html', locations=data_columns[3:])

if __name__ == "__main__":
    app.run(debug=True)