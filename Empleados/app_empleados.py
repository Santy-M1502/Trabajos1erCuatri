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
#     # agregar sueldo!!!!!!!
#     empleados.append(new_empleado(legajo, nombre, apellido, genero, edad, calle, localidad, provincia, email, sector))
# mostrar_empleados(empleados)

cargar_empleados(empleados, TAM)
# ordenar_empleados_triple_criterio(empleados)
mostrar_empleados(empleados)



#PUNTOS TAREAS PROFE----------------------
#0 pedir un legajo y mostrar al empleado con ese legajo
buscar_nombre_por_legajo(empleados)

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#1 mostrar por consola los nombres y sectores de los empleados
for e in range(TAM):
    print(f"{empleados[e]["nombre"]} - {empleados[e]["sector"]}")

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#2 pedir un sector y mostrar los empleados de ese sector
print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#3 pedir un sector y mostrar el promedio de los sueldos de ese sector
print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#4 mostrar el promedio de sueldos de cada uno de los sectores
print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#5 mostrar el empleados que mas gana y a que sector pertenece
print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#6 mostrar el empleado o los empleados que tienen el mail mas corto y cuantos caracteres tiene
print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#7 decir cual es el sector que mas sueldo cobra
print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#8 decir cual es el sector que mas empleados tiene
print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#9 ordenar empleados por sector, dentro de un sector por genero y dentro del genero por legajo descendente







