import threading
import time

#Manejo de paralelismo e hilos de proceso
'''def tarea(nombre):
    print(f"Inicio de la raeas: {nombre}")
    time.sleep(2) #Tiempo de espera de ejecucion del hilo
    print(f"Fin del hilo de proceso: {nombre}")

hilo1 = threading.Thread(target=tarea, args=("Hilo1",))
hilo2 = threading.Thread(target=tarea, args=("Hilo2",))

hilo1.start() #Para iniciar el proceso para los tiempos de espera
hilo2.start()

hilo1.join() #para cerrar el proceso del tiempo de espera
hilo2.join()

print("Todos los hilos han terminado ")'''

#Multiproceso o multiples hilos de proceso
from multiprocessing import Process
import time

def tarea_calulo(numero):
    print(f"Inicio del calculo: {numero}")
    suma = sum(i*i for i in range(10000000))
    print(f"Resultado del calculo {numero}: {suma}")

#Manejo de los procesos especificados en la deficiocion 
if __name__ =="__main__":
    proceso1 = Process(target=tarea_calulo, args=(1,))
    proceso2 = Process(target=tarea_calulo, args=(2,))
    proceso1.start()
    proceso2.start()
    proceso1.join()
    proceso2.join()
    print("Todos los procesos han terminado")

import threading
import multiprocessing
import time

def suma_grande(inicio, fin):
    suma = sum(range(inicio, fin))
    return suma

inicio_tiempo = time.time()
resultado_secuencial1 = suma_grande(0, 1000000000)
fin_tiempo = time.time()

print(f"Suma secuencial: {resultado_secuencial1}, tiempo: {fin_tiempo - inicio_tiempo:.2f}")

inicio_tiempo =time.time()
hilo1 = threading.Thread(target=suma_grande, args=(0, 500000000))
hilo2 = threading.Thread(target=suma_grande, args=(500000000, 1000000000))

hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()
fin_tiempo1 = time.time()
print(f"tiempo: {fin_tiempo - inicio_tiempo:.2f} segundos")

inicio_tiempo = time.time()
if __name__ == "__main__":
    proceso1 = multiprocessing.Process(target=suma_grande, args=(0, 500000000))
    proceso2 = multiprocessing.Process(target=suma_grande, args=(500000000, 1000000000))

    proceso1.start()
    proceso2.start()
    proceso1.join()
    proceso2.join()
    fin_tiempo = time.time()
print(f"tiempo con multiprocessing: {fin_tiempo - inicio_tiempo:.2f} segundos")