from funciones_empleados import *

TAM = 5
empleados = []


# for _ in range(TAM):
#     legajo = int(input("Ingrese el legajo: "))
#     nombre = input("Ingrese el nombre: ")
#     apellido = input("Ingrese el apellido: ")
#     genero = input("Ingrese el genero: ")
#     edad = int(input("Ingrese edad: "))
#     calle = input("Ingrese calle: ")
#     localidad = input("Ingrese localidad: ")
#     provincia = input("Ingrese provincia: ")
#     email = input("Ingrese email: ")
#     sector = input("Ingrese sector: ")
#     empleados.append(new_empleado(legajo, nombre, apellido, genero, edad, calle, localidad, provincia, email, sector))
# mostrar_empleados(empleados)

cargar_empleados(empleados, TAM)

mostrar_empleados(empleados)




