#matriz materias x alumnos  6x500
import time
import numpy as np
#Variar estos datos para analizar los tiempos de ejecución.

materias = 6 #se pueden cambiar estos valores por: 100, 500, 10000
alumnos = 500 #se pueden cambiar estos valores por: 1000, 10000, 100000

matriz = np.random.randint(0, 101, size=(materias, alumnos))

def buscar_alumno(matriz, materia, alumno):
    valor = matriz[materia-1][alumno-1]
    return valor, (materia-1, alumno-1)

inicio = time.time()
for _ in range(100000):
    resultado, indices = buscar_alumno(matriz, 6, 322) 
fin = time.time()
print("matriz materias x alumnos  6x500")
print(f"Tiempo de ejecución (materia x alumno) en 100,000 búsquedas: {fin - inicio} segundos")
print(f"Alumno buscado: {resultado}, posición = {indices}")

