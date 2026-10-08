import pickle
#datos = {"nombre": "Denisse", "Edad": 30, "Ciudad": "Durango"} #genera un archivo binario con los datos

#with open("datos.pickle", "wb") as archivo: #
    #pickle.dump(datos, archivo)

'''with open("datos.pickle", "rb") as archivo:
    datos_recuperados = pickle.load(archivo)
    print(datos_recuperados)'''

import json
# Creamos el archivo de datos a partir del json
'''datos = {"nombre": "Denisse", "Edad": 30, "Ciudad": "Durango"}

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)'''

# Abrimos el archivo creado
'''with open("datos.json", "r") as archivo:
    datos_recuperados = json.load(archivo)
    print(datos_recuperados)'''

#importamos pickle y json
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    def __repr__(self):
        return f"{self.nombre}, {self.edad} años, {self.ciudad}"

personas = [Persona("Ana", 28, "Tepic"), Persona("Jesus", 32, "Guadalajara")]

with open("personas.pickle", "wb") as archivo:
   pickle.dump(personas, archivo)   

personas_json = [{"nombre": p.nombre, "edad": p.edad, "ciudad": p.ciudad} for p in personas]

with open("personas.json", "w") as archivo:
    json.dump(personas_json, archivo, indent=4)

with open("personas.pickle", "rb") as archivo:
    personas_recuperadas_pickle = pickle.load(archivo)
    print("Deserializacion con pickle", personas_recuperadas_pickle)

with open("personas.json", "r") as archivo:
    personas_recuperadas_json = json.load(archivo)
    print("Deserializacion con json", personas_recuperadas_json)