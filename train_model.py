import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load and validate dataset
data = pd.read_csv("insurance.csv")
if (data['charges'] < 0).any():
    print("Warning: Negative charges found in dataset. Filtering them out.")
    data = data[data['charges'] >= 0]

# Preprocessing
data['sex'] = data['sex'].map({'male': 0, 'female': 1})
data['smoker'] = data['smoker'].map({'yes': 1, 'no': 0})
data['region'] = data['region'].map({'northeast': 0, 'northwest': 1, 'southeast': 2, 'southwest': 3})
X = data.drop('charges', axis=1)
y = data['charges']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model.pkl')
print("Model saved as model.pkl")
