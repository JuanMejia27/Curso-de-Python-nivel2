import sqlite3
import json

with open("usuarios.json", "r") as file:
    usuarios = json.load(file)

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER,
        ciudad TEXT
    )
""")

for usuario in usuarios:
    cursor.execute(
        "INSERT INTO usuarios (nombre, edad, ciudad) VALUES (:nombre, :edad, :ciudad)",
        usuario
    )

conn.commit()

cursor.execute('SELECT * FROM usuarios')
resultados = cursor.fetchall()
print("Datos: ")
for row in resultados:
    print(row)

conn.close()