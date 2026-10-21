from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np

#datos con poco sesgo, es tratar de que no supere el 0.5%
x = np.array([[50], [60], [80], [100], [120]])
y = np.array([100000,120000,160000,200000,240000])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(x_train, y_train)

y_pred = modelo.predict(x_test)

error = mean_absolute_error(y_test, y_pred)
print("Error medio absoluto: ", error)
 #Este toma una media a partir del valor que se de y te da un aproximado con los datos que se tienen de prueba
print("Precio estimado para una casa de 90m'2", modelo.predict([[90]])[0])