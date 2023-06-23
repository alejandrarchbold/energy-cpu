import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate sample data
data = pd.read_csv('output.csv')
data.info()

def tiempo_a_segundos(tiempo):
    minutos, segundos = map(float, tiempo.split(':'))
    total_segundos = minutos * 60 + segundos
    return total_segundos
    
data['TIME'] = data['TIME+'].apply(tiempo_a_segundos)

data['%CPU'] = data['%CPU'].str.replace(',', '.')
data['%MEM'] = data['%MEM'].str.replace(',', '.')

data['%CPU'] = data['%CPU'].astype(float)
data['%MEM'] = data['%MEM'].astype(float)

data['Energy'] = data['%CPU'] * data['%MEM'] / 1000

# Convertir kilobytes a megabytes
data['VIRT_MB'] = data['VIRT'] / 1024
data['RES_MB'] = data['RES'] / 1024
data['SHR_MB'] = data['SHR'] / 1024

    
# Extract independent variables (CPU usage, memory usage, and I/O operations)
X = data[['VIRT_MB', 'RES_MB', 'SHR_MB', 'TIME']]

# Extract dependent variable (energy consumption)
y = data['Energy']

# Crear un array de pesos basado en la variable "TIME"
weights = 1 / data['TIME']

# Ajustar modelo de regresión ponderada
weighted_model = LinearRegression().fit(X, y, sample_weight=weights)

# Ajustar modelo de regresión lineal simple
linear_model = LinearRegression().fit(X, y)

# Predecir valores con ambos modelos
y_pred_weighted = weighted_model.predict(X)
y_pred_linear = linear_model.predict(X)

# Calcular el error cuadrático medio (MSE) para ambos modelos
mse_weighted = np.mean((y - y_pred_weighted) ** 2)
mse_linear = np.mean((y - y_pred_linear) ** 2)


# Print the MSE
print("MSE linear:", mse_linear)
print("MSE weighted:", mse_weighted)


### Plots

data_X = data[data['COMMAND'] == 'nodo_pid.py']
data_Y = data[data['COMMAND'] == 'ekf_localizatio']

# Convertir las columnas de tiempo y energía en matrices NumPy
time_X = np.array(data_X['TIME'])
energy_X = np.array(data_X['Energy'])
time_Y = np.array(data_Y['TIME'])
energy_Y = np.array(data_Y['Energy'])

# Crear las gráficas de energía a lo largo del tiempo para X y Y
plt.plot(time_X, energy_X, label='nodo_pid.py')
plt.plot(time_Y, energy_Y, label='ekf_localizatio')
plt.xlabel('Time')
plt.ylabel('Energy')
plt.legend()
plt.title('Compare the estimated energy from the Python executable with the energy plots from the ROS simulator.')
plt.show()



