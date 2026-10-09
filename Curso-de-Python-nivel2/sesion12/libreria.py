import sqlite3

conexion = sqlite3.connect("libros.db")
cursor = conexion.cursor()

#cursor.execute('''
#CREATE TABLE IF NOT EXISTS libros(
#            id INTEGER PRIMARY KEY AUTOINCREMENT,
#            titulo TEXT NOT NULL,
#            autor TEXT NOT NULL,
#            año_publicacion INTEGER
#            )
#''')

#cursor.execute('''
#INSERT INTO libros(titulo, autor, año_publicacion)
#VALUES ("El alquimista", "paulo Coelho", 1988)
#''')

#cursor.execute('''
#INSERT INTO libros(titulo, autor, año_publicacion)
#VALUES ("1984", "George", 1945)
#''')

#cursor.execute('''
#INSERT INTO libros(titulo, autor, año_publicacion)
#VALUES ("La sombra del viento", "Ruiz", 1990)
#''')

#conexion.commit()
#conexion.close()

cursor.execute("SELECT * FROM libros WHERE año_publicacion > 1950")
libros_recientes = cursor.fetchall()
for libro in libros_recientes:
    print(libro)

cursor.execute('''
UPDATE libros
SET autor = "Ruiz Saavedra"
WHERE id = 3
''')

cursor.execute('''
DELETE FROM libros WHERE titulo = "1984"
''')
conexion.commit()
conexion.close()