from Data_warehouse import *
from FuncionesListas import *
from random import randint

LEGAJO = 0
NOMBRE = 1
GENERO = 2
NOTAP1 = 3
NOTAP2 = 4
PROMEDIO = 5

def calcular_promedio(valor1:int, valor2:int)->float:#CHECK
    promedio = (valor1 + valor2) / 2
    return promedio

def cargar_datos_en_lista(lista_destino:list, lista_origen:list)->None:
    if isinstance(lista_destino,list):
            lista_destino.append(lista_origen)
    else:
        raise ValueError("Eso no es una lista")

def cargar_notas_lista(lista:list)->None:
    if isinstance(lista,list):
        cargar_lista_enteros_random(lista, 1, 0, 10)
    else:
        raise ValueError("Eso no es una lista")

def promediar_listas(lista:list)->None:
    if isinstance(lista,list):
        lista.append(calcular_promedio(lista[-1], lista[-2]))
    else:
        raise ValueError("Eso no es una lista")

def cargar_legajos_lista(lista:list)->None:
    legajo_min = 20000
    legajo_max = 30000
    from random import randint
    if isinstance(lista,list):
        lista.append(randint(legajo_min, legajo_max))
    else:
        raise ValueError("Eso no es una lista")

def cargar_alumnos(alumnos:list, cantidad:int):
    if isinstance(alumnos,list):
        for i in range(cantidad):
            j = randint(0, 25)
            alumnos.append([])
            cargar_legajos_lista(alumnos[i])
            cargar_datos_en_lista(alumnos[i], nombres_lista[j])
            cargar_datos_en_lista(alumnos[i], generos_lista[j])
            cargar_notas_lista(alumnos[i])
            cargar_notas_lista(alumnos[i])
            promediar_listas(alumnos[i])
    else:
        raise ValueError("Eso no es una lista")

def mostrar_alumno(un_alumno:list):
    print(f"  {un_alumno[LEGAJO]}     {un_alumno[NOMBRE]}{un_alumno[GENERO]}{un_alumno[NOTAP1]}{un_alumno[NOTAP2]}   {un_alumno[PROMEDIO]}") 

def mostrar_alumnos(alumnos:list)->None:
        print("                             ***Lista de alumnos***")
        print("  Legajo       Nombre      Genero          NotaP1          NotaP2          Promedio")
        print("------------------------------------------------------------------------------------")
        cant = len(alumnos)
        for i in range(cant):
            mostrar_alumno(alumnos[i])
        print()
        
def definir_campo_alumno(campo:str)->int:
    match campo:
        case "l":
            retorno = LEGAJO
        case "n":
            retorno = NOMBRE
        case "g":
            retorno = GENERO
        case "p":
            retorno = PROMEDIO
        case _: raise ValueError("No es un campo valido")
    return retorno


def ordenar_alumnos(alumnos, campo, asc:bool = True):
    atributo = definir_campo_alumno(campo)
    tam = len(alumnos)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if alumnos[i][atributo] > alumnos[j][atributo] if asc else alumnos[i][atributo] < alumnos[j][atributo]:
                swap_lista(alumnos, i, j)   

def ordenar_alumnos_doble_criterio(alumnos:list):

    tam = len(alumnos)
    for i in range(tam-1):
        for j in range ( i+1, tam):
            if alumnos[i][GENERO] == alumnos[j][GENERO]:
                if alumnos[i][LEGAJO] > alumnos[j][LEGAJO]:
                    swap_lista(alumnos, i, j)
            elif alumnos[i][GENERO] > alumnos[j][GENERO]:
                    swap_lista(alumnos, i, j)


def new_alumno(legajo, nombre, genero, nota_p1, nota_p2):
    nuevo_alumno = []
    nuevo_alumno.append(legajo)
    nuevo_alumno.append(nombre)
    nuevo_alumno.append(genero)
    nuevo_alumno.append(nota_p1)
    nuevo_alumno.append(nota_p2)
    nuevo_alumno.append(calcular_promedio(nota_p1, nota_p1))
    return nuevo_alumno
