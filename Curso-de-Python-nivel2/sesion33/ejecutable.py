import numpy as np
import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression 
#from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.metrics import accuracy_score, confusion_matrix    
import seaborn as sns

#Generar una grafica de puntos
'''np.random.seed(42)
x = np.random.randn(50, 1)*100
y = 4*x+20+np.random.randn(50, 1)*30

plt.scatter(x, y, color = "blue", label = "Datos simulados")
plt.xlabel("Tamaño de la casa")
plt.ylabel("Datos para regresion lineal")
plt.legend()
plt.show()

#Generar otra grafica de puntos para los datos
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
mse = mean_absolute_error(y,y_pred)
r2 = r2_score(y, y_pred)

plt.scatter(x, y, color = "blue", label = "Datos simulados")
plt.plot(x, y_pred, color="red", label="Linea de regresion")
plt.xlabel("Tamaño de la casa")
plt.ylabel("Precio de la casa")
plt.title(f"Rgresion linea: MSE = {mse:.2f}, R'2 = {r2:.2f}")
plt.legend()
plt.show()'''

#Puntos aleatorios y metrica de cumplimiento
np.random.seed(42)
x = np.random.rand(100,2)
y = (x[:,0] + x[:,1] > 1).astype(int)

plt.scatter(x[:,0],x[:,1], c = y, cmap="coolwarm", label="Datos simulados")
plt.xlabel("caracteristicas1")
plt.ylabel("caracteristicas2")
plt.title("Datos para clasificacion")
plt.legend()
plt.show()

model = LogisticRegression()
model.fit(x, y)

y_pred = model.predict(x)

accuracy = accuracy_score(y, y_pred)
conf_matrix = confusion_matrix(y, y_pred)

sns.scatterplot(x=x[:,0], y=x[:,1], hue=y_pred, palette="coolwarm")
plt.title(f"Clasificacion basica: Precision={accuracy:.2f}")
plt.xlabel("caracteristicas1")
plt.ylabel("caracteristicas2")
plt.legend()
plt.show()

sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d", xticklabels=["Clase 0", "Clase 1"], yticklabels=["Clase 0", "Clase 1"])
plt.title("Matriz de confusion")
plt.xlabel("Prediccion")
plt.ylabel("Real")
plt.show()