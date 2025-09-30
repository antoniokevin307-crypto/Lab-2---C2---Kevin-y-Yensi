
import pandas as pd
import numpy as np

# 1. Cargar el dataset (asegurate que el archivo esté en la misma carpeta del .py)
df = pd.read_csv("futbolresultados.csv")

# 2. Resumen de los datos con describe()
print("----- Resumen con describe() -----")
print(df.describe(include="all"))   # incluye tanto numéricos como texto
print("\n")

# 3. Tipos de datos con dtypes
print("----- Tipos de datos (dtypes) -----")
print(df.dtypes)
print("\n")
print("Comentario: con esta info se sabe qué columnas son números (para operaciones) y cuáles son texto (para conteo o agrupación)")
print("\n")

# 4. Mostrar primeros y últimos registros (head y tail)
print("----- Primeros 5 registros -----")
print(df.head())
print("\n")

print("----- Últimos 5 registros -----")
print(df.tail())
print("\n")

# 5. Ordenar resultados (ejemplo: por la primera columna numérica que encuentre)
columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()

if columnas_numericas:
    col = columnas_numericas[0]  # agarramos la primera numérica
    print(f"----- Ordenado por {col} (menor a mayor) -----")
    print(df.sort_values(by=col, ascending=True).head(10))
    print("\n")

    print(f"----- Ordenado por {col} (mayor a menor) -----")
    print(df.sort_values(by=col, ascending=False).head(10))
    print("\n")
else:
    print("No hay columnas numéricas para ordenar")
    print("\n")

# 6. Medidas estadísticas en una columna numérica
if columnas_numericas:
    col = columnas_numericas[0]
    print(f"----- Medidas estadísticas en la columna '{col}' -----")
    print("Media:", np.mean(df[col]))
    print("Mediana:", np.median(df[col]))
    print("Desviación estándar:", np.std(df[col]))  # std poblacional
    print("\n")
else:
    print("No hay columnas numéricas para calcular medidas")
