import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv(r"C:\Users\Dell\Downloads\heart+disease\heart.csv.data")

# Assign column names
columns = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
    'restecg', 'thalach', 'exang', 'oldpeak', 'slope',
    'ca', 'thal', 'target'
]
data.columns = columns

# Replace missing values (in dataset `?`) with NaN and drop rows with NaN
data = data.replace("?", pd.NA)
data = data.dropna()

# Convert columns to numeric
for col in data.columns:
    data[col] = pd.to_numeric(data[col])

# Binary classification: 0 = no disease, 1 = disease
data['target'] = data['target'].apply(lambda x: 1 if x > 0 else 0)

# Split data
X = data.drop("target", axis=1)
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save model
joblib.dump(model, "model/heart_model.pkl")
print("✅ Model saved to model/heart_model.pkl")
