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
    try:
        # Retrieve and validate input data from the form
        age = int(request.form['age'])
        sex = request.form['sex']
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']

        # Validate inputs
        if sex not in ['male', 'female']:
            raise ValueError("Invalid sex value")
        if smoker not in ['yes', 'no']:
            raise ValueError("Invalid smoker value")
        if region not in ['northeast', 'northwest', 'southeast', 'southwest']:
            raise ValueError("Invalid region value")
        if age < 0 or bmi < 0 or children < 0:
            raise ValueError("Numeric inputs cannot be negative")
        bmi = max(15, min(50, bmi))  # Clamp BMI to reasonable range

        # Preprocess the input
        sex_value = 0 if sex == 'male' else 1
        smoker_value = 1 if smoker == 'yes' else 0
        region_map = {'northeast': 0, 'northwest': 1, 'southeast': 2, 'southwest': 3}
        region_value = region_map[region]

        # Create the input data for prediction
        input_data = pd.DataFrame([[age, sex_value, bmi, children, smoker_value, region_value]],
                                  columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

        # Predict the insurance cost
        prediction = max(0, model.predict(input_data)[0])  # Ensure non-negative

        # Load and render index.html with prediction and form data
        with open('index.html', 'r') as file:
            html_content = file.read()
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
    except (ValueError, KeyError) as e:
        # Load and render index.html with error message
        with open('index.html', 'r') as file:
            html_content = file.read()
        return render_template_string(html_content, error=str(e))
if __name__ == '__main__':
    app.run(debug=True)
