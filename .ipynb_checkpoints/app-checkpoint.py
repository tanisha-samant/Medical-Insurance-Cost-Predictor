from flask import Flask, request, render_template, send_from_directory
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
import os

app = Flask(__name__, template_folder='.', static_folder='.')

# Load the model
model = joblib.load('model.pkl')

# Initialize LabelEncoder
le = LabelEncoder()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/style.css')
def serve_css():
    return send_from_directory('.', 'style.css')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        features = {
            'age': int(request.form['age']),
            'sex': request.form['sex'],
            'bmi': float(request.form['bmi']),
            'children': int(request.form['children']),
            'smoker': request.form['smoker'],
            'region': request.form['region']
        }
        
        # Create a DataFrame
        df = pd.DataFrame([features])
        
        # Encode categorical variables
        df['sex'] = le.fit_transform(df['sex'])
        df['smoker'] = le.fit_transform(df['smoker'])
        df['region'] = le.fit_transform(df['region'])
        
        # Make prediction
        prediction = model.predict(df)[0]
        
        return render_template('result.html', 
                             prediction=f"${prediction:,.2f}",
                             features=features)
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)