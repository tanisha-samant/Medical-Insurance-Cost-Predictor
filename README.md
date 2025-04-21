# Medical Insurance Cost Predictor

This is a Flask web application that predicts medical insurance costs based on user input. It utilizes a pre-trained model, which predicts insurance charges based on various factors such as age, sex, BMI, number of children, smoking status, and region.

## Features

- User-friendly web interface for inputting data.
- Predicts insurance costs based on user inputs.
- Displays results in a clear and informative way.

## Demo
![Image](https://github.com/user-attachments/assets/cb3f79a1-20fc-4f58-93a6-dd68b8378a6e)

![Image](https://github.com/user-attachments/assets/bb418456-3ca9-43d2-a38b-6d81df472c3b)

## Technologies Used

- **Python**: The programming language used to build the application.
- **Flask**: A lightweight WSGI web application framework for Python.
- **scikit-learn**: A machine learning library used for creating the predictive model.
- **Pandas**: A data manipulation and analysis library for Python.
- **NumPy**: A library for numerical computations in Python.
- **joblib**: A library for saving and loading the trained model.

## Installation

Follow these steps to get a copy of the project up and running on your local machine:

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/Medical_Insurance_Cost_Prediction.git
   cd Medical_Insurance_Cost_Prediction# Medical Insurance Cost Predictor
2. **Create a virtual environment (optional but recommended)**:
   ```bash
   conda create --name myenv python=3.8
   conda activate myenv
3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
4. **Prepare the model**:
   Make sure you have insurance.csv in the project directory.
   Run the training script to create the model:
   ```bash
   python train_model.py
## Usage
1. Run the Flask application:
   ```bash
   python app.py
2. Open your web browser and go to http://127.0.0.1:5000.
3. Fill out the form with the required information and click "Predict Insurance Cost" to see the prediction.
