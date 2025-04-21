from flask import Flask, render_template_string, request, send_from_directory
import joblib
import pandas as pd
import os

# Create the Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# Define a route for the home page
@app.route('/')
def index():
    # Load the HTML content from the index.html file directly
    with open('index.html', 'r') as file:
        html_content = file.read()
    return render_template_string(html_content)

# Define a route to serve the CSS file directly
@app.route('/static/<filename>')
def serve_css(filename):
    return send_from_directory(os.getcwd(), filename)

# Define a route for the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve input data from the form
    age = int(request.form['age'])
    sex = request.form['sex']
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = request.form['smoker']
    region = request.form['region']
    
    # Preprocess the input
    sex_value = 0 if sex == 'male' else 1
    smoker_value = 1 if smoker == 'yes' else 0
    region_map = {'northeast': 0, 'northwest': 1, 'southeast': 2, 'southwest': 3}
    region_value = region_map[region]
    
    # Create the input data for prediction
    input_data = pd.DataFrame([[age, sex_value, bmi, children, smoker_value, region_value]],
                          columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
    
    # Predict the insurance cost
    prediction = model.predict(input_data)[0]
    
    # Load the HTML content and insert the prediction result
    with open('index.html', 'r') as file:
        html_content = file.read()
    
    # Return the HTML content with the prediction and form data
    return render_template_string(html_content, 
                                 prediction=round(prediction, 2),
                                 form_data={
                                     'age': age,
                                     'sex': sex,
                                     'bmi': bmi,
                                     'children': children,
                                     'smoker': smoker,
                                     'region': region
                                 })

if __name__ == '__main__':
    app.run(debug=True)
