#Carga de datos y exploracion

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

x,y = make_classification(n__examples=1000, n_features=2, n_informative=2,n_redundant=0, random_state=42)
data = pd.DataFrame(x, columns=["Edad", "Salario"])
data["Compra"] = y

print(data.head())
print(data.describe())

plt.scatter(data["Edad"], data["Salario"], c = y, cmap="coolwarm", edgecolors="k")
plt.title("Distribucion inicial")
plt.xlabel("Edad")
plt.ylabel("Salario")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_sclaed = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_sclaed, y, test_size=0.2, random_state=42)

print(f"Tamaño del conjunto de entrenamiento: {x_train.shape[0]}")
print(f"Tamaño del conjunto de prueba: {x_test.shape[0]}")

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

logreg = LogisticRegression(random_state=42)
logreg.fit(x_train, y_train)

y_pred = logreg.predict(x_test)
print("Reporte de clasificacion: ")
print(classification_report(y_test, y_pred))

accuracy = accuracy_score(y_test, y_pred)
print(f"Precision inicial: {accuracy:.2f}")

from sklearn.model_selection import GridSearchCV

param_grid = {"C": [0.01, 0.1, 1, 10, 100], "solver": ["lbfgs", "liblinear"]}

grid_search = GridSearchCV(LogisticRegression(random_state=42), param_grid, cv=5, scoring="accuracy")
grid_search.fit(x_train, y_train)

best_model = grid_search.best_estimator_
print("Mejores hiperparametros: ", grid_search.best_params_)

y_pred_best = best_model.predict(x_test)
print("Reporte de clasificacion del mejor modelo: ")
print(classification_report(y_test, y_pred_best))

from sklearn.metrics import roc_curve, auc

y_prob = best_model.predict_proba(x_test)[:,1]
fpr, tpr, _= roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr, color = "blue", label=f"Curva de roc(Auc = {roc_auc:.2f})")
plt.plot([0,1],[0,1], color="gray", linestyle="--")
plt.title("Curva Roc")
plt.xlabel("Tasa de falsos positivos")
plt.ylabel("Tasa de verdaderos positivos")
plt.legend(loc = "lower right")
plt.show()