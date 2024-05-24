from FuncionesListas import *
from Funciones_paralelas import *


TAM = 5

legajos = []
nombres = []
generos = []
notas_p1 = []
notas_p2 = []
promedios = []

cargar_alumnos(legajos, nombres, generos, notas_p1, notas_p2, promedios, TAM)

for i in range(TAM):
    print(legajos[i], nombres[i], generos[i], notas_p1[i], notas_p2[i], promedios[i])
    
print("--------------------")

ordenar_alumnos(legajos, nombres, generos, notas_p1, notas_p2, promedios)
for i in range(TAM):
    print(legajos[i], nombres[i], generos[i], notas_p1[i], notas_p2[i], promedios[i])

print("--------------------")

mostrar_alumnos(legajos, nombres, generos, notas_p1, notas_p2, promedios)
