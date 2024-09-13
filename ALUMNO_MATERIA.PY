#matriz alumnos x materias 500x6
import time
import numpy as np
#Variar estos datos para analizar los tiempos de ejecución.

alumnos = 100000 #se pueden cambiar estos valores por: 1000, 10000, 100000
materias = 10000 #se pueden cambiar estos valores por: 100, 500, 10000

matriz = np.random.randint(0, 101, size=(alumnos,materias))

def buscar_alumno(matriz, materia, alumno):
    valor = matriz[alumno-1][materia-1]
    return valor, (alumno-1, materia-1)

inicio = time.time()
for _ in range(100000):
    resultado, indices = buscar_alumno(matriz,6,322) 
fin = time.time()

print("#matriz alumnos x materias 500x6")
print(f"Tiempo de ejecución (materia x alumno) en 100,000 búsquedas: {fin - inicio} segundos")
print(f"Alumno buscado: {resultado}, posición = {indices}")
