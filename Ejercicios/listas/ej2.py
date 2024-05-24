from FuncionesListas import *

# lista = []
# CANT = 5
# MIN = 1
# MAX = 10
# cargar_lista_enteros_random(lista, CANT, MIN, MAX)
# mostrar_lista(lista)

# promedio = calcular_promedio(lista)
# print(f"El promedio de la lista es {promedio}")

# try:
#     numeros = [1, 2, 3]
#     total = calcular_promedio(numeros)
#     print(total)
# except ValueError as e:
#     print(e)

# lista = [1, 3, 5, 4]
# try:
#     mayor = calcular_mayor(lista)
#     print(mayor)
# except ValueError as e:
#     print(e)

# lista = [10, 5, 3, 1, 8]
# menor = calcular_menor(lista)
# print(menor)

# lista = [1, 3, 6, 7, 9]
# numero = entero_in_lista(lista, 6)
# print(numero)

lista = crear_lista_enteros_random(10, 0, 10)
print(lista)
busca = buscar_in_lista(lista, 2)
print(busca)
contar = contar_in_lista(lista, 2)
print(contar)
