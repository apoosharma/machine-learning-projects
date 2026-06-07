from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Read all 8 features from form
    features = [
        float(request.form['MedInc']),
        float(request.form['HouseAge']),
        float(request.form['AveRooms']),
        float(request.form['AveBedrms']),
        float(request.form['Population']),
        float(request.form['AveOccup']),
        float(request.form['Latitude']),
        float(request.form['Longitude']),
    ]

    scaled = scaler.transform([features])          # scale before predict
    prediction = model.predict(scaled)[0]
    price = round(prediction * 100000, 2)          # convert from $100k units

    return render_template('index.html', prediction=f"Estimated House Price: ${price:,}")

if __name__ == '__main__':
    app.run(debug=True)