import pandas as pd
from sklearn.linear_model import LinearRegression

# Collect energy consumption and runtime data
# You can use an energy monitoring tool and a profiling tool to collect the data

# Define the runtime and energy consumption data as Pandas dataframes
# runtime_data is the independent variable (X)
# energy_data is the dependent variable (Y)
runtime_data = pd.DataFrame({'Runtime': [0.0005, 0.0007, 1.2, 1.4, 1.6, 1.8, 2.0]})
energy_data = pd.DataFrame({'Energy': [0.0, 0.0, 5.4, 6.2, 6.8, 7.2, 7.8]})

# Perform linear regression
regressor = LinearRegression()
regressor.fit(runtime_data, energy_data)

# Print the regression coefficients
print('Regression coefficient (intercept):', regressor.intercept_[0])
print('Regression coefficient (slope):', regressor.coef_[0][0])

# Estimate energy consumption for a new runtime value
new_runtime = 0.0006
predicted_energy = regressor.predict([[new_runtime]])
print('Estimated energy consumption for runtime', new_runtime, ':', predicted_energy[0][0], 'Joules')
