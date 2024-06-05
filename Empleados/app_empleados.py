from funciones_empleados import *

TAM = 20
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
# ordenar_empleados(empleados, "l")
# mostrar_empleados(empleados)
# print(busqueda_binaria_empleado_legajo(20002, empleados))



# # PUNTOS TAREAS PROFE----------------------
# # 0 pedir un legajo y mostrar al empleado con ese legajo
# buscar_nombre_por_legajo(empleados)

# print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
# #1 mostrar por consola los nombres y sectores de los empleados
# mostrar_lista_tuplas(mapear_lista(lambda emp: (emp["nombre"],emp["sector"]), empleados))

# print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
# # #2 pedir un sector y mostrar los empleados de ese sector
# sector = "Sistemas"
# empleados_sistemas = filtrar_lista(lambda emp: (emp["sector"]) == sector, empleados)
# mostrar_empleados(empleados_sistemas)

# if len(empleados_sistemas) > 0:
#     mostrar_empleados(empleados_sistemas)
# else:
#     print(f"No hay empleados de {sector}")

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
# 3 pedir un sector y mostrar el promedio de los sueldos de ese sector
# promedio_sueldo_por_sector(empleados)
# sector = "Contabilidad"
# empleados_contabilidad = filtar_empleados_sector(empleados,sector)
# sueldos = mapear_campo(empleados_contabilidad, "sueldo")
# promedio = calcular_promedio(sueldos)
# print(f"Promedio sueldo sector {sector}: ${promedio}")

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
# 4 mostrar el promedio de sueldos de cada uno de los sectores
# for sector in sectores:
#     empleados_sector = filtar_empleados_sector(empleados, sector)
#     sueldos = mapear_campo(empleados_sector, "sueldo")
#     promedio = calcular_promedio(sueldos)
#     print(f"Promedio sueldo sector {sector}: ${promedio}")
#     print("----------------------------")

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#5 mostrar el empleados que mas gana y a que sector pertenece
# empleado_sector_mayor_sueldo(empleados)

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#6 mostrar el empleado o los empleados que tienen el mail mas corto y cuantos caracteres tiene
# emails = mapear_campo(empleados, "email")
# email_corto = []
# email_flag = True
# for el in emails:
#     if email_flag == True or len(el) < len(email_corto[0]):
#         email_corto = []
#         email_corto.append(el)
#         email_flag = False
# print(email_corto)


print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#7 decir cual es el sector que mas sueldo cobra
# sector_mas_cobra(empleados)

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#8 decir cual es el sector que mas empleados tiene
pass

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")
#9 ordenar empleados por sector, dentro de un sector por genero y dentro del genero por legajo descendente
# ordenar_empleados_triple_criterio(empleados)
# mostrar_empleados(empleados)



