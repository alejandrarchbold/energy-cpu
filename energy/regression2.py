import pandas as pd
from sklearn.linear_model import LinearRegression

# Generate sample data
data = pd.read_csv('output.csv')
data.info()
# Extract independent variables (CPU usage, memory usage, and I/O operations)
X = data[['%CPU', '%MEM']]

# Extract dependent variable (energy consumption)
y = data['Energy']

# Fit linear regression model
model = LinearRegression().fit(X, y)

# Predict energy consumption for new input values
new_X = [[8.0, 1], [6.0, 0.5]]
predicted_y = model.predict(new_X)

print('predicciones:',predicted_y)
