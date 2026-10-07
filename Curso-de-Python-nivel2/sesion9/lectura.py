import csv
# Manejo de archivos CSV
datos = [["nombre","edad","ciudad"], ["Juan","25","Madrid"], ["Maria","30","Barcelona"], ["Pedro","28","Valencia"]]

with open("datos.csv", mode="w", newline="") as archivos: # Escribir los datos
    escritor = csv.writer(archivos)
    escritor.writerows(datos)

with open("datos.csv", newline="") as archivo: # Leer los datos
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

import json
# Manejo de archivos JSON
datos= {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

with open("datos1.json", "w") as archivo: # Escribir los datos
    json.dump(datos, archivo, indent=4)

#with open("datos1.json", "r") as archivo:
try:
    with open("datos1.json", "r") as archivo:
        datos = json.load(archivo)
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON, formato no válido.")

# Manejo de archivos XML
import xml.etree.ElementTree as ET

raiz =  ET.Element("Personas")
persona1 = ET.SubElement(raiz, "persona", nombre = "Ana")
persona1.text = "29 anios, Guadalajara"
persona2 = ET.SubElement(raiz, "persona", nombre = "Esli")
persona2.text = "30 anios, Durango"

arbol = ET.ElementTree(raiz)
arbol.write("datos2.xml")

tree = ET.parse("datos2.xml")
raiz = tree.getroot()

for elemento in raiz:
    print(elemento.tag, elemento.attrib)

import csv

'''empleados=[
    {"ID":1, "Nombre":"Ana", "Edad":28, "Departamento": "Ventas"},
    {"ID":2, "Nombre":"Carlos", "Edad":29, "Departamento": "Ventas"},
    {"ID":3, "Nombre":"Esli", "Edad":30, "Departamento": "RH"},
    {"ID":4, "Nombre":"Amairani", "Edad":32, "Departamento": "Ventas"},
    {"ID":5, "Nombre":"Jose", "Edad":27, "Departamento": "Sistemas"},
    {"ID":6, "Nombre":"Alejandro", "Edad":28, "Departamento": "Sistemas"},{"ID":7, "Nombre":"Juan", "Edad":32, "Departamento": "Desarrollador"},
    ]

with open("empleados.csv", mode="w", newline="") as archivo_csv:
    campos = ["ID","Nombre", "Edad", "Departamento"]
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(empleados)

# Uso de imports csv y json
empleados_leidos = []

with open("empleados.csv", mode="r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        fila["ID"] = int(fila["ID"])
        fila["Edad"] = int(fila["Edad"])
        empleados_leidos.append(fila)

with open("empleados.json", mode="w") as archivo_json:
    json.dump(empleados_leidos, archivo_json, indent=4)
    print("Datos convertidos con exito")'''

############################################################
'''with open("empleados.json", mode="r") as archivo_json:
    datos_json = json.load(archivo_json)

nuevo_empleado = {"ID":8, "Nombre":"Carlos", "Edad":31, "Departamento": "Soporte"}
datos_json.append(nuevo_empleado)

with open("empleados.json", mode="w") as archivo_json:
    json.dump(datos_json, archivo_json, indent=4)'''

# import xml.etree.ElementTree as ET, json
with open("empleados.json", mode="r") as archive_json:
    empleados_json = json.load(archive_json)

raiz = ET.Element("Empleados")

for empleado in empleados_json:
    elemento_empleado = ET.SubElement(raiz, "empleados", id=str(empleado["ID"]))
    nombre = ET.SubElement(elemento_empleado, "Nombre")
    nombre.text = empleado["Nombre"]
    edad = ET.SubElement(elemento_empleado, "Edad")
    edad.text = str(empleado["Edad"])
    departamento = ET.SubElement(elemento_empleado, "Departamento")
    departamento.text = empleado["Departamento"]

arbol = ET.ElementTree(raiz)
arbol.write("empleados.xml", encoding="utf-8", xml_declaration=True)