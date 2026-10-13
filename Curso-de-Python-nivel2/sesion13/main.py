'''from utilities.math_operations import add
from utilities.string_operations import capitalizar

print(add(2,3))
print(capitalizar("Hola, como estas?"))'''

#importacion con alias para el archivo de operaciones
'''import utilities.math_operations as mo

resultado = mo.add(7,3)
print(resultado)
'''

#Para imporar todo del archivo es:
from utilities.math_operations import *
from utilities.string_operations import *

resultado = multiplicar(7,3)
print(resultado)

print(reverse("Hola"))

#cambio de ruta de importacion
from utilities.advanced.calculus import *

print(integrate())