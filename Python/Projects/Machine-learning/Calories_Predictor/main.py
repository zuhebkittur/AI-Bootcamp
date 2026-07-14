import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ==========================================
# Load CSV File
# ==========================================

current_folder = os.path.dirname(__file__)
csv_path = os.path.join(current_folder, "runner_data.csv")

df = pd.read_csv(csv_path)

print("=" * 60)
print("AI CALORIES PREDICTOR")
print("=" * 60)

print(df)

print()

print(f"Rows       : {df.shape[0]}")
print(f"Columns    : {df.shape[1]}")
print(f"Column Names : {list(df.columns)}")
print()

print(df.dtypes)


X = df[["Distance"]]
y = df["Calories"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)



print("=" * 50)
print("Actual      Predicted")
print("=" * 50)

for actual, predicted in zip(y_test, predictions):
    print(f"{actual:<10} {predicted:.2f}")

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error : {mae:.2f}")

print(model.coef_)
print(model.intercept_)