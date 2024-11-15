import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Create sample data
np.random.seed(42)
n_samples = 1000

data = {
    'age': np.random.randint(18, 65, n_samples),
    'sex': np.random.choice(['male', 'female'], n_samples),
    'bmi': np.random.normal(26, 4, n_samples),
    'children': np.random.randint(0, 5, n_samples),
    'smoker': np.random.choice(['yes', 'no'], n_samples),
    'region': np.random.choice(['northeast', 'northwest', 'southeast', 'southwest'], n_samples),
    'charges': np.random.normal(13000, 5000, n_samples)
}

df = pd.DataFrame(data)

# Prepare the features
le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])
df['smoker'] = le.fit_transform(df['smoker'])
df['region'] = le.fit_transform(df['region'])

# Separate features and target
X = df.drop('charges', axis=1)
y = df['charges']

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
joblib.dump(model, 'model.pkl')
print("Model trained and saved successfully!")