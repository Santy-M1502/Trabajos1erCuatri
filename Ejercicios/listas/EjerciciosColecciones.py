from FuncionesListas import crear_lista_enteros_random, buscar_par_listas, lista_mayor10_filtro
from os import system

def menu()->str:
    limpiar_pantalla()
    print("        Ordenar")
    print("1-Ordenar de forma ascendente ")
    print("2-Ordenar de forma descendente ")
    print("3-Salir ")
    return  input("Ingrese opcion: ")

def pausar():
    system("pause")

def limpiar_pantalla():
    system("cls")

def menu()->str:
    limpiar_pantalla()
    print("        Ingresar Numeros")
    print("1-Ingresar valor ")
    print("2-Salir ")
    return  input("Ingrese opcion: ")

numeros = crear_lista_enteros_random(10, 1, 100)
pares = buscar_par_listas(numeros)
print(f"Los numeros pares de la lista son: {pares}")

lista = []

while True:
    match menu():
        case "1":
            limpiar_pantalla
            numero_ingresado = int(input("Ingrese un numero "))
            lista.append(numero_ingresado)
        case "2":
            break

print(lista_mayor10_filtro(lista))