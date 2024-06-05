def menuO():
    print("        Ordenar")
    print("1-Ordenar de forma ascendente ")
    print("2-Ordenar de forma descendente ")
    return  input("Ingrese opcion: ")

def duplicar(numero:int)->int:
    numero = numero * 2
    return numero

def mostrar_lista_tuplas(listas:list)->None:
    for tupla in listas:
        for el in tupla:
            print(f"{el:15}", end="")
        print()

def duplicar_valores(lista)->None:
    for i in range(len(lista)):
        lista[i] = lista[i] * 2
    
def mostrar_lista(lista:list)->None:
    if isinstance(lista, list):
        for el in lista:
            print(el, end=" ")
        print()
    else:
        raise ValueError("Eso no es una lista")

def cargar_lista_enteros_random(lista:list, cant:int, desde:int, hasta:int)->None:
    if isinstance(lista, list):
        from random import randint
        for _ in range(cant):
            lista.append(randint(desde, hasta))
    else:
        raise ValueError("Eso no es una lista")

def crear_lista_enteros_random(cant:int, desde:int, hasta:int)->list:
    from random import randint
    lista = []
    cargar_lista_enteros_random(lista, cant, desde, hasta)
    return lista

def totalizar_lista(lista:list)->int:
    if isinstance(lista, list):
        total = 0
        for el in lista:
            total += el
        return total
    raise ValueError("Eso no es una lista")

def calcular_promedio(lista:list)->float:
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("No esta definido el promedio de una lista vacia")
        return totalizar_lista(lista) / cant
    raise ValueError("Eso no es una lista")

def calcular_mayor(lista:list)->int:
    if isinstance(lista,list):
        if len(lista) == 0:
            raise ValueError("La lista esta vacia")
        mayor = lista[0]
        for i in range(1, len(lista)):
            if lista[i] > mayor:
                mayor = lista[i]
        return mayor
    raise ValueError ("No es una lista")

def calcular_menor(lista:list)->int:
    if isinstance(lista,list):
        if len(lista) == 0:
            raise ValueError("La lista esta vacia")
        menor = lista[0]
        for i in range(1, len(lista)):
            if lista[i] < menor:
                menor = lista[i]
        return menor
    raise ValueError ("No es una lista")

def entero_in_lista(lista:list, target:int)->bool:
    if isinstance(lista,list):
        if len(lista) == 0:
            raise ValueError ("La lista esta vacia")
        target_contador = False
        for el in lista:
            if el == target:
                target_contador = True
                break
        return target_contador
    raise ValueError ("No es una lista")

def buscar_in_lista(lista:list, target:int)->int: 
    if isinstance(lista, list):
        if len(lista) == 0:
            raise ValueError("La lista esta vacia")
        contador = 0
        for i in lista:
            if i == target:
                break
            contador += 1
        if contador == len(lista):
            contador = -1
        return contador
    raise ValueError ("Eso no es una lista")

def contar_in_lista(lista:list, target:int)->int: 
    if isinstance(lista,list):
        if len(lista) == 0:
            raise ValueError ("La lista esta vacia")
        contador_target = 0
        for el in lista:
            if el == target:
                contador_target += 1
        return contador_target
    raise ValueError ("Eso no es una lista")

def buscar_par_listas(lista:list)->list:
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("La lista esta vacia")
        lista_pares = []
        for x in lista:
            if (x % 2 == 0):
                lista_pares.append(x)
        return lista_pares
    raise ValueError("Eso no es una lista")

def lista_mayor10_filtro(lista:list):
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("La lista esta vacia")
        lista_10 = []
        for x in lista:
            if (x > 10):
                lista_10.append(x)
        cant10 = len(lista_10)
        if cant10 == 0:
            return ("Ningun numero ingresado es mayor a 10")
        return lista_10
    raise ValueError("Eso no es una lista")

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

def swap_lista(lista:list, valor1, valor2):
    aux = lista[valor1]
    lista[valor1] = lista[valor2]
    lista[valor2] = aux
