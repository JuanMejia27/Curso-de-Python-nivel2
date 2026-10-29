'''OPTIMIZACIÓN Y ANÁLISIS DE RENDIMIENTO'''
'''import timeit
codigo = """
suma = 0
for i in range(1000):
    suma += i
"""

#nos da el tiempo
print(timeit.timeit(codigo, number=10000))'''

'''@profile
def calcular():
    suma = 0
    for i in range(1000):

ejemplos de codigo sin optimizar y optimizado'''


'''resultado = []

for i in range(1000):
    if i not in resultado:
        resultado.append()

resultado = set()
for i in range(1000):
    resultado.add(i)'''

def calcular_suma(n): 
    return sum((i*(i-10)//2 for i in range(n)))


if __name__ == '__main__':
    print(calcular_suma(1000))                 