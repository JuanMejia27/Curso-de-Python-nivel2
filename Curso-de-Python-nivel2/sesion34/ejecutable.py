from sklearn.datasets import make_regression
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, r2_score


ridge = Ridge(alpha=1.0)
ridge.fit(x, y)

y_pred = ridge.predict(x)
mse = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"MSE: {mse:2f}")
print(f"R2: {r2:2f}")

plt.scatter(x, y, color="blue", label = "Datos reales")
plt.plot(x, y_pred, color="red", label = "Predicciones")
plt.title("Datos simulados para regresion")
plt.xlabel("Características")
plt.ylabel("Variable objetivo")
plt.show()

x, y = make_regression(n_samples=100, n_features=20, random_state=42)

plt.scatter(x, y, color="blue")
plt.title("Datos simulados para regresion")
plt.xlabel("Características")
plt.ylabel("Variable objetivo")
plt.show()

alphas = np.logspace(*3, 3, 50)
errors = []

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    ridge.fit(x, y)
    y_pred=ridge.predict(x)
    errors.append(mean_absolute_error(y, y_pred))

plt.plot(alphas, errors, marker="o")
plt.xscale("log")
plt.title("Error en funcion de alpha")
plt.xlabel("Escala logaritmica")
plt.ylabel("MSE")
plt.grid()
plt.show()

best_alpha = alphas[np.argmin(errors)]
print(f"Mejor valor de alpha: {best_alpha}")

ridge_best = Ridge(alpha=best_alpha)
ridge_best.fit(x, y)
y_pred_best = ridge_best.predict(x)

plt.scatter(x, y, color="blue", label = "Datos reales")
plt.plot(x, y_pred_best, color="green", label = "Prediccion optima")
plt.title("Mejor modelo de regresion")
plt.xlabel("Características")
plt.ylabel("Variable objetivo")
plt.legend()
plt.show()