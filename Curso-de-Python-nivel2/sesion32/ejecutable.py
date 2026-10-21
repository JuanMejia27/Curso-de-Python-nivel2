from sklearn.datasets import load_iris
import pandas as pd
#Agregamos otra importacion
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, classification_report

iris = load_iris()
x = iris.data
y = iris.target

#Muestra las opciones de la libreria de machine learning
iris_df = pd.DataFrame(x, columns=iris.feature_names)
iris_df['species'] = iris.target_names[y]
print(iris_df.head())

#Fikltrado y limpiado de datos
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

print(pd.DataFrame(x_scaled, columns=iris.feature_names).head())

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=72)

print(f"Tamaño del conjunto de entrenamiento: {x_train.shape}")
print(f"Tamaño de conjunto de prueba: {x_test.shape}")

imputer = SimpleImputer(strategy='mean')
x_imputer = imputer.fit_transform(x)

#Interacion hasta obtener datos precisos
'''knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)'''
for k in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    print(f"Precision del {k}: {accuracy_score(y_test, y_pred)}")

#y_pred = knn.predict(x_test)
#print("Precision del modelo: ", accuracy_score(y_test, y_pred))
print("Reporte de calificacion: ", classification_report(y_test, y_pred, target_names=iris.target_names))

'''regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
print("Error cuadratico medio: ", mean_absolute_error(y_test, y_pred))
'''