import asyncio
import time
import threading
import multiprocessing
import math


def simular_descarga_sync(id_tarea):
    """Simula una espera de red I/O de 1 segundo."""
    time.sleep(1)
    return f"Tarea I/O {id_tarea} completada"

async def simular_descarga_async(id_tarea):
    """Simula una espera de red I/O de manera asíncrona."""
    await asyncio.sleep(1)
    return f"Tarea I/O {id_tarea} completada"


def probar_io_threading(cantidad_tareas=10):
    inicio = time.time()
    hilos = []
    
    for i in range(cantidad_tareas):
        hilo = threading.Thread(target=simular_descarga_sync, args=(i,))
        hilos.append(hilo)
        hilo.start()
        
    for hilo in hilos:
        hilo.join()
        
    fin = time.time()
    print(f"⏱️ [I/O-Bound] Threading ({cantidad_tareas} tareas): {fin - inicio:.2f} segundos")

async def probar_io_asyncio(cantidad_tareas=10):
    inicio = time.time()
    tareas = [simular_descarga_async(i) for i in range(cantidad_tareas)]
    await asyncio.gather(*tareas)
    fin = time.time()
    print(f"⏱️ [I/O-Bound] Asyncio ({cantidad_tareas} tareas): {fin - inicio:.2f} segundos")



def calcular_factoriales_pesados(n=30000):
    """Tarea intensiva en CPU."""
    return math.factorial(n)


def probar_cpu_secuencial(repetir=4):
    inicio = time.time()
    for _ in range(repetir):
        calcular_factoriales_pesados()
    fin = time.time()
    print(f"⏱️ [CPU-Bound] Secuencial: {fin - inicio:.2f} segundos")

def probar_cpu_threading(repetir=4):
    inicio = time.time()
    hilos = []
    for _ in range(repetir):
        hilo = threading.Thread(target=calcular_factoriales_pesados)
        hilos.append(hilo)
        hilo.start()
        
    for hilo in hilos:
        hilo.join()
        
    fin = time.time()
    print(f"⏱️ [CPU-Bound] Threading (Afectado por GIL): {fin - inicio:.2f} segundos")

def probar_cpu_multiprocessing(repetir=4):
    inicio = time.time()
    procesos = []
    for _ in range(repetir):
        p = multiprocessing.Process(target=calcular_factoriales_pesados)
        procesos.append(p)
        p.start()
        
    for p in procesos:
        p.join()
        
    fin = time.time()
    print(f"⏱️ [CPU-Bound] Multiprocessing (Aprovecha Multinúcleo): {fin - inicio:.2f} segundos")


if __name__ == "__main__":
    print("====== 1. PRUEBAS DE TAREAS I/O-BOUND ======")
    print("Simulando 10 descargas (Cada una toma 1 segundo de espera):")
    probar_io_threading(10)
    asyncio.run(probar_io_asyncio(10))
    
    print("\n====== 2. PRUEBAS DE TAREAS CPU-BOUND ======")
    print("Calculando 4 factoriales de gran tamaño:")
    probar_cpu_secuencial(4)
    probar_cpu_threading(4)
    probar_cpu_multiprocessing(4)