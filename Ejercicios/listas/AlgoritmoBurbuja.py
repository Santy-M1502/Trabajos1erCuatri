from FuncionesListas import *
from os import system

def pausar():
    system("pause")

def limpiar_pantalla():
    system("cls")

def menuO():
    print("        Ordenar")
    print("1-Ordenar de forma ascendente ")
    print("2-Ordenar de forma descendente ")
    return  input("Ingrese opcion: ")

def ordenar_lista_ascendente(lista:list)->None:
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def ordenar_lista_descendente(lista:list)->None:
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def ordenar_lista(lista:list):
    if isinstance(lista, list):
        match menuO():
            case "1":
                listaB = ordenar_lista_ascendente(lista)
            case "2":
                listaB = ordenar_lista_descendente(lista)
            case _:
                raise ValueError("Debe responder con el numero de una de las opciones")
    else:
        raise TypeError("Se esperaba una lista")
    return listaB

try:
    lista = crear_lista_enteros_random(10, 0, 100)
    print(ordenar_lista(lista))
except ValueError as e:
    print(e)
