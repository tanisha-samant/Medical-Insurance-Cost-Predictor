# Medical Insurance Cost Predictor

This project is a Flask-based web application that predicts medical insurance costs using a pre-trained machine learning model. By inputting personal details such as age, sex, BMI, number of children, smoking status, and region, users can estimate their potential insurance charges.

## Project Overview
Predicting medical insurance costs is crucial for both individuals and insurance companies. This application leverages machine learning to provide cost estimates based on various personal attributes.

## Features

- **User-Friendly Interface**: Input personal details via a web form.
- **Real-Time Predictions**: Get instant insurance cost estimates.
- **Model Integration**: Utilizes a pre-trained model for accurate predictions.
- **Responsive Design**: Accessible on both desktop and mobile devices.

## Technologies Used

- **Python**: The programming language used to build the application.
- **Flask**: A lightweight WSGI web application framework for Python.
- **scikit-learn**: A machine learning library used for creating the predictive model.
- **Pandas**: A data manipulation and analysis library for Python.
- **NumPy**: A library for numerical computations in Python.
- **joblib**: A library for saving and loading the trained model.

## Project Structure

```bash
├── app.py               # Flask application
├── index.html           # Frontend form
├── result.html          # Prediction result page
├── insurance.csv        # Dataset for training
├── model.pkl            # Trained machine learning model
├── requirements.txt     # Python dependencies
├── Procfile             # Heroku deployment file
├── train_model.py       # Script to train the model
├── style.css            # Custom styles
└── README.md            # Project documentation
```

## Setup & Installation

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
3. Fill out the form with the required information and click "Predict" to see the prediction.

## Dataset Information
The model is trained on the Medical Cost Personal Dataset from Kaggle, which includes the following features:
- **age**: Age of the primary beneficiary
- **sex**: Gender of the policyholder
- **bmi**: Body Mass Index
- **children**: Number of children/dependents covered by health insurance
- **smoker**: Smoking status (yes/no)
- **region**: Residential area in the US
- **charges**: Medical costs billed by health insurance

## Model Details
The project employs a machine learning model trained using Scikit-learn. The model is serialized using Joblib and can be found as model.pkl. The training process involves data preprocessing, feature encoding, and model evaluation.

## Demo
![Image](https://github.com/user-attachments/assets/cb3f79a1-20fc-4f58-93a6-dd68b8378a6e)

![Image](https://github.com/user-attachments/assets/bb418456-3ca9-43d2-a38b-6d81df472c3b)
