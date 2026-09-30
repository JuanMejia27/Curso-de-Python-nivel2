'''try:
    z = 1/0
except ZeroDivisionError:
    print("NO ES POSIBLE DIVIDIR ENTRE CERO")'''

'''try:
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un numero: "))
    resultado =a//b
    print(resultado)
except ValueError:
    print("Se esperaba un numero entero")
except ValueError:
    print("NO ES POSIBLE DIVIDIR ENTRE CERO")
#except Exception as e:
#    print(f"Ha ocurrideo un error: {e}")
else: #se puede utilizar para las condiciones del try
    print(f"El resultado de la division es: {resultado}")'''

'''try:
    archivo = open("datos.txt","r")
    contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo fue encontrado")
finally:
    archivo.close()
    print("El archivo se ha cerrado")'''

def validar_edad(edad):
    if edad < 18:
        raise ValueError("La edad debe ser mayor o igual a 18")
    else:
        print("Edad valida")

try:
    edad_usuario = int(input("Ingresar su edad: "))
    validar_edad(edad_usuario)
except ValueError as e:
    print(f"Error: {e}")