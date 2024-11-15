# Medical Insurance Cost Prediction

This is a Flask web application that predicts medical insurance costs based on user input. It utilizes a pre-trained model, which predicts insurance charges based on various factors such as age, sex, BMI, number of children, smoking status, and region.

## Features

- User-friendly web interface for inputting data.
- Predicts insurance costs based on user inputs.
- Displays results in a clear and informative way.

## Demo
![Screenshot 2024-11-15 194955](https://github.com/user-attachments/assets/404a60c8-5970-4d8e-858b-51112d6900cb)

![Screenshot 2024-11-15 195006](https://github.com/user-attachments/assets/8b91c239-3de6-4063-b199-951f9fd0e0a7)

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
5. **Run the Flask application**:
   ```bash
   python app.py
