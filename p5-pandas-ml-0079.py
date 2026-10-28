import numpy as np
import pandas as pd

# Iram Jimenez NC = 0079 Fecha 28/10/2026
## Datos matriz 4 x 3
datos_alumno = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]
# Poner nombre a las columnas
# y almacenar la tabla en la variable df
df = pd.DataFrame(datos_alumno, columns=['ci', 'marcas', 'paquete'])
print(df)
#Datos a partir de un diccionario
alumno_diccionario = {
    'nombre' : ["Iram", "Andres", "Ramses", "Stephanie", "Alex", "Hugo"],
    "califa" : [60, 90, 100, 80, 70, 50],
    "Edad" : [16, 16, 15, 16, 10, 17]
}

estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)

print("Iram Jimenez NC = 0079")