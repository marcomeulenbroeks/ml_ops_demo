import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os
from datetime import datetime

# Read the dataset
df = pd.read_csv('data/ice_cream_sales_dataset.csv')

# Prepare features and target variable
X = df[['temperature_celsius', 'num_tourists']]
y = df['ice_creams_sold']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Performance:")
print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.2f}")

# Save the model
os.makedirs('models', exist_ok=True)
model_filename = "models/linear_model.pkl"
joblib.dump(model, model_filename)

print(f"Model saved as: {model_filename}")

# Log metrics
os.makedirs('metrics', exist_ok=True)
metrics_file = "metrics/history.csv"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

new_metrics = pd.DataFrame({
    'timestamp': [timestamp],
    'mse': [mse],
    'r2_score': [r2]
})

if os.path.exists(metrics_file):
    existing_metrics = pd.read_csv(metrics_file)
    combined_metrics = pd.concat([existing_metrics, new_metrics], ignore_index=True)
else:
    combined_metrics = new_metrics

combined_metrics.to_csv(metrics_file, index=False)
print(f"Metrics logged to: {metrics_file}")