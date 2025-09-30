# Laboratorio 2 Segundo Cómputo – Semana 10
# Objetivo: 
Desarrollar soluciones a problemas mediante el análisis de datos utilizando la librería de pandas.
# Docente: 
 - Willian Alexis Montes Girón
# Integrantes: 
 - Yensi Elizabeth Valladares Ventura
 - Kevin Antonio Castro Araujo
# Preguntas:
# a. Describe brevemente de qué trata el dataset utilizado:
El dataset contiene resultados de partidos internacionales de fútbol masculino desde 1872 hasta 2025, incluyendo mundiales, copas y amistosos. Cada fila es un partido con datos como fecha, equipos, goles, torneo, ciudad, país y si fue en campo neutral.

# b. ¿Qué información permite ver el resumen estadístico?
El resumen estadístico (describe()) muestra la cantidad de registros, los valores mínimos y máximos, la media de goles, y en columnas de texto indica cuántos valores distintos hay (equipos, torneos, países). Esto da una idea rápida de la distribución de los datos y su variedad.

# c. ¿Qué cambios o tendencias se detectan en la información del dataset?
Al revisar los primeros y últimos registros se nota que:
- Los partidos han pasado de ser pocos y en torneos muy puntuales (finales del siglo XIX) a miles de encuentros en distintas competiciones modernas.
- También se amplió la variedad de torneos y países participantes, mostrando un crecimiento global del fútbol.

# d. ¿Qué categorías sobresalen en la comparación y por qué crees que será?
- En columnas como torneo sobresalen la Copa Mundial de la FIFA y partidos de clasificación, porque son los más disputados y con mayor número de registros.
- En equipos, suelen sobresalir selecciones históricas (Brasil, Alemania, Argentina, Italia), ya que han jugado más partidos y llegan más lejos en torneos internacionales.

# e. ¿Qué diferencias se observan entre los primeros y últimos registros?
- Los primeros registros (1870s) son pocos, con equipos europeos como Inglaterra y Escocia.
- Los últimos registros (2020s) muestran una gran diversidad de selecciones y torneos internacionales, reflejando la expansión del fútbol a nivel mundial.

f. ¿Qué aportan las medidas estadísticas al análisis del dataset?
Las medidas (media, mediana, desviación estándar) permiten ver:
- El promedio de goles que se marcan en un partido.
- Qué tan común es un resultado “típico” (mediana).
- Qué tanta variabilidad hay en los resultados (si hay goleadas o partidos cerrados).
