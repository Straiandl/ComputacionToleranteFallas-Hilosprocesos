# Práctica: Concurrencia, Paralelismo y Benchmarking en Python

## Descripción General

Este proyecto implementa una herramienta de benchmarking (*Benchmark Tool*) para evaluar y comparar de manera práctica las distintas técnicas de programación concurrente y paralela en Python: **`threading`**, **`multiprocessing`** y **`asyncio`**.

A través de esta práctica se analiza el comportamiento del rendimiento ante dos tipos de cargas de trabajo:
1. **Operaciones I/O-Bound (Entrada/Salida):** Simulación de peticiones de red o descargas.
2. **Operaciones CPU-Bound (Procesamiento Intensivo):** Cálculos matemáticos pesados para evidenciar el impacto del **GIL (Global Interpreter Lock)** de Python.

---

##  Objetivos de la Práctica

* Diferenciar conceptual y prácticamente entre **Concurrencia** (manejo de múltiples tareas superpuestas) y **Paralelismo** (ejecución simultánea en múltiples núcleos de CPU).
* Demostrar de forma empírica cómo el **GIL** limita la ejecución multihilo en tareas intensivas de CPU.
* Analizar cuándo es conveniente aplicar `threading`, `multiprocessing` o `asyncio` según la naturaleza del problema.

---

## Resumen Comparativo de Métodos

| Técnica | Tipo de Tarea Recomendada | Mecanismo | Impacto del GIL |
| :--- | :--- | :--- | :--- |
| **`threading`** | I/O-Bound | Hilos del sistema operativo en un solo proceso. | **Liberado** durante esperas de I/O. Ineficaz para CPU. |
| **`multiprocessing`** | CPU-Bound | Múltiples procesos independientes con memoria propia. | **Evasión completa del GIL** (un GIL por proceso). |
| **`asyncio`** | I/O-Bound (Alto volumen) | Bucle de eventos (*Event Loop*) sobre un solo hilo. | **N/A** (No usa múltiples hilos, cede control con `await`). |

---

## Resultados.

### 1. Resultados de Rendimiento en Consola (I/O-Bound)
![(https://github.com/Straiandl/ComputacionToleranteFallas-Hilosprocesos/blob/6d14b164a030371e5aa2d4c5af003c8ce08a3b0d/Hilos1.png)]

### 2. Demostración del Impacto del GIL (CPU-Bound)
*Captura de los tiempos comparativos entre la ejecución Secuencial, `threading` (bloqueado por el GIL) y `multiprocessing` (paralelismo real):*
![https://github.com/Straiandl/ComputacionToleranteFallas-Hilosprocesos/blob/6d14b164a030371e5aa2d4c5af003c8ce08a3b0d/Hilos2.png)]


---

##  Cómo Ejecutar el Benchmark

1. Abre la terminal en la carpeta raíz del proyecto.
2. Asegúrate de tener Python 3.7 o superior (no requiere librerías externas ya que utiliza la biblioteca estándar de Python).
3. Ejecuta el script principal:

   ```bash
   python benchmark_concurrencia.py
   ```

---
