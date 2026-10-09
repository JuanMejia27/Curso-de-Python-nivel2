import sqlite3

conexion = sqlite3.connect("mi_base_de_datos.db")
print("Conexion a BD exitosa")

#cursor = conexion.cursor()
#cursor.execute('''
#CREATE TABLE IF NOT EXISTS
#    empleados(
#            id INTEGER PRIMARY KEY AUTOINCREMENT,
#            nombre TEXT NOT NULL,
#            edad INTEGER,
#            departamento TEXT
#            )
#''')
#
#cursor.execute('''
#INSERT INTO empleados(nombre, edad, departamento)
#VALUES('Juan Mejia', 30, 'Sistemas')
#                ''')
#conexion.commit() #Para guardar los cambios
#print("Tabla 'empleados' creada")

cursor = conexion.cursor()

#cursor.execute('''
#INSERT INTO empleados(nombre, edad, departamento)
#VALUES('Daniela Urias', 28, 'Finanzas')
#''')
#conexion.commit()

#cursor.execute("SELECT * FROM empleados")
#resultados = cursor.fetchall()
#for fila in resultados:
#    print(fila)

#cursor.execute(" SELECT nombre, edad FROM empleados")
#cursor.execute(" SELECT nombre, departamento FROM empleados")
#empleados = cursor.fetchall()
#for empleado in empleados:
#    print(empleado)

#cursor.execute("select * from empleados where edad<25") # puede ser en mayusculas o minusculas las sentencias SQL pero se recomienda usar mayusculas para distinguirlos
#empleados_mayores = cursor.fetchall()
#for empleado in empleados_mayores:
#    print(empleado)

cursor = conexion.execute('''
UPDATE empleados
SET edad = 30
WHERE ID = 1
''')
# WHERE nombre = "Juan Mejia" puede ser por nombre ID u otro parametro

cursor.execute('''
DELETE FROM empleados WHERE ID = 1
''')

conexion.commit() #Para guardar los cambios

conexion.close()