from sklearn.linear_model import LinearRegression

X = [
    [2],
    [4],
    [6],
    [8],
    [10]
]

y = [
    150,
    300,
    450,
    600,
    750
]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[12]])

print(f"Predicted Calories : {prediction[0]:.2f}")