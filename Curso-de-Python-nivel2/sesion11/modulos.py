import os # Para moverse entre directorios y archivos
#archivo = "ejemplo.txt"
'''if os.path.exists(archivo): # Busca el archivo para ver si este existe
    print(f"{archivo} existe")
else:
    print(f"{archivo} no existe")

tama = os.path.getsize(archivo)
print(f"El tamaño de {archivo} es {tama} bytes") #Muestra el tamaño dela rchivo

ruta_absoluta = os.path.abspath(archivo)
print(f"La ruta absoluta del {archivo} es {ruta_absoluta}") #obtiene la tuta del archivo 

#os.mkdir("Nuevo_directorio") #Crear nueva carpeta/Directorio
#print("Disrectorio 'nuevo_directorio' creado")

os.chdir("nuevo_directorio")
print(f"EL directorio actual es: {os.getcwd()}") #Muestra la direccion actual de la carpeta mecionada

archivos = os.listdir()
print(f"Archivos en el directorio: {archivos}") #Muestra el contenido de la carpeta/directorio

os.remove("eliminar.txt")
print(f"Archivo 'eliminar.txt' fue eliminado") # Eliminar en la ruta principal

os.rmdir("nuevo_directorio") # Eliminar carpeta/directorio
print("Directorio 'nuevo_directorio' eliminado")'''

import shutil

'''shutil.copy("origen.txt", "copia.txt") # Genera una copia de un archivo
print("Archivo copiado con exito")

shutil.copytree("hola", "hola2")
print("Directorio copiado")

shutil.move("origen.txt", "hola/origen.txt")
print("Archivo movido")

shutil.move("hola2", "hola")
print("Directorio movido")

shutil.rmtree("hola")''' # Elimina la carpeta

#import os y shutil

#Primero ejecutamos este codigo
'''os.mkdir("mi_directorio") #Craear dorectorio

for i in range(1, 4):
    with open(f"mi_directorio/archivo{i}.txt", "w") as f:
        f.write(f"Este es el contenido del archivo {i}.\n")'''

#Despues este para realizar una copia del directorio y todos los archivos
'''os.mkdir("copia_directorio")
for i in range(1,4):
    shutil.copy(f"mi_directorio/archivo{i}.txt", "copia_directorio")

os.mkdir("archivos_mover")
shutil.move("copia_directorio/archivo1.txt", "archivos_mover/archivo1.txt")'''

#Eliminar todo
shutil.rmtree("mi_directorio")
shutil.rmtree("copia_directorio")
shutil.rmtree("archivos_mover")