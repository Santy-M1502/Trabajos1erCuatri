from Funciones_paralelas_renovadas import *
TAM = 1

alumnos = []


for i in range(TAM):
    legajo = int(input("Ingrese el legajo: "))

    nombre = input("Ingrese el nombre: ")

    genero = input("Ingrese el genero: ")

    nota1 = int(input("Ingrese la primer nota: "))

    nota2 = int(input("Ingrese la segunda nota: "))

    alumnos.append(new_alumno(legajo, nombre, genero, nota1, nota2))

mostrar_alumnos(alumnos)