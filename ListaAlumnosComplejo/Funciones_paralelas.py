from Data_warehouse import *
from FuncionesListas import *

def calcular_promedio(valor1:int, valor2:int)->float:
    promedio = (valor1 + valor2) / 2
    return promedio

def mostrar_alumnos(legs:list, names:list, genders:list, notes_p1:list, notes_p2:list, proms:list)->None:
    if isinstance(legs,list):
        print("                             ***Lista de alumnos***")
        print("  Legajo       Nombre      Genero          NotaP1          NotaP2          Promedio")
        print("------------------------------------------------------------------------------------")
        cant = len(legs)
        for i in range(cant):
            mostrar_alumno(legs[i], names[i], genders[i], notes_p1[i], notes_p2[i], proms[i])
    else:
        raise ValueError("Eso no es una lista")

def cargar_datos_en_lista(lista_destino:list, lista_origen:list, cant)->None:
    if isinstance(lista_destino,list):
        for i in range(cant):
            lista_destino.append(lista_origen[i])
    else:
        raise ValueError("Eso no es una lista")

def cargar_notas_lista(lista:list, cantidad:int)->None:
    if isinstance(lista,list):
        lista_numeros = cargar_lista_enteros_random(lista, cantidad, 0, 10)
    else:
        raise ValueError("Eso no es una lista")

def promediar_listas(lista_a:list, lista_b:list, lista_promedio:list)->None:
    if isinstance(lista_a,list):
        for i in range(len(lista_a)):
            lista_promedio.append(calcular_promedio(lista_a[i], lista_b[i]))
    else:
        raise ValueError("Eso no es una lista")

def cargar_legajos_lista(lista:list, cantidad:int)->None:
    legajo_min = 20000
    legajo_max = 30000
    from random import randint
    if isinstance(lista,list):
        while cantidad > len(lista):
            legajo = randint(legajo_min, legajo_max)
            flag_en_lista = False

            for elemento in lista:
                if elemento == legajo:
                    flag_en_lista = True
                    break
            
            if flag_en_lista == False:
                lista.append(legajo)
    else:
        raise ValueError("Eso no es una lista")


def ordenar_alumnos(legs:list, names:list, genders:list, notes_p1:list, notes_p2:list, proms:list)->None: #ordenar de mas a menos por promedio
    if isinstance(legs,list):
        for i in range(len(proms)):
            for j in range(i + 1):
                if proms[j] < proms[i]:
                    swap_lista(legs, i, j)
                    swap_lista(names, i, j)
                    swap_lista(genders, i, j)
                    swap_lista(notes_p1, i, j)
                    swap_lista(notes_p2, i, j)
                    swap_lista(proms, i, j)
    else:
        raise ValueError("Eso no es una lista")

def cargar_alumnos(legs:list, names:list, gender:list, notesP1:list, notesP2:list, proms:list, cantidad:int)->None:
    if isinstance(legs,list):
        cargar_legajos_lista(legs, cantidad)
        cargar_datos_en_lista(names, nombres_lista, cantidad)
        cargar_datos_en_lista(gender, generos_lista, cantidad)
        cargar_notas_lista(notesP1, cantidad)
        cargar_notas_lista(notesP2, cantidad)
        promediar_listas(notesP1, notesP2, proms)
    else:
        raise ValueError("Eso no es una lista")
    
def mostrar_alumno(legajo, nombre, genero, nota_1, nota_2, promedio):
    print(f"{legajo:^10}   {nombre:^10}   {genero:^10}      {nota_1:^10}      {nota_2:^10}      {promedio:^10}")

if __name__ == "__main__":
    print("Hola, lo hiciste mal :D")
