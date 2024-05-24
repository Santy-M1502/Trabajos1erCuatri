from FuncionesListas import *
from random import randint, choice
from data_empleados import *


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

def cargar_empleados(lista:list, cantidad:int):
    LEGAJO_INICIAL = 20000
    EDAD_MIN = 18
    EDAD_MAX = 65
    next_legajo = LEGAJO_INICIAL
    if isinstance(lista,list):
        for _ in range(cantidad):
            legajo = next_legajo
            next_legajo += 1
            genero = choice(["f", "m"])
            nombre = choice(nombres_m) if genero == "m" else choice(nombres_f)
            apellido = choice(apellidos)
            edad = randint(EDAD_MIN, EDAD_MAX)
            calle = f"Calle:{randint(100, 500)} nro:{randint(1000, 3000)}"
            localidad = choice(localidades)
            provincia = choice(provincias)
            sector = choice(sectores)
            email = f"{nombre.lower()}{apellido.lower()}{choice(dominios)}"
            lista.append(new_empleado(legajo, nombre, apellido, genero, edad, calle, localidad, provincia, email, sector))
    else:
        raise ValueError("Eso no es una lista")

def mostrar_empleado(un_empleado:dict):
    print(f"  {un_empleado["legajo"]}   {un_empleado["nombre"]}   {un_empleado["apellido"]}      {un_empleado["genero"]}        {un_empleado["edad"]}   {un_empleado["localidad"]}   {un_empleado["provincia"]}   {un_empleado["email"]}         {un_empleado["sector"]}   {un_empleado["calle"]}  ") 

def mostrar_empleados(empleados:list)->None:
        print("                             ***Lista de empleados***")
        print("  Legajo   Nombre  Apellido      Genero   Edad     Porvincia     Email            Calle         Sector       Localidad")
        print("-----------------------------------------------------------------------------------------------------------------------")
        cant = len(empleados)
        for i in range(cant):
            mostrar_empleado(empleados[i])
        print()
        
def definir_campo_alumno(campo:str)->str:
    match campo:
        case "l":
            retorno = "legajo"
        case "n":
            retorno = "nombre"
        case "g":
            retorno = "genero"
        case "s":
            retorno = "sector"
        case "loc":
            retorno = "localidad"
        case "p":
            retorno = "provincia"
        case _: raise ValueError("No es un campo valido")
    return retorno


def ordenar_empleados(empleados, campo, asc:bool = True):
    atributo = definir_campo_alumno(campo)
    tam = len(empleados)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if empleados[i][atributo] > empleados[j][atributo] if asc else empleados[i][atributo] < empleados[j][atributo]:
                swap_lista(empleados, i, j)   

def ordenar_empleados_triple_criterio(empleados:list):

    tam = len(empleados)
    for i in range(tam-1):
        for j in range ( i+1, tam):
            if empleados[i]["sector"] == empleados[j]["sector"]:
                if empleados[i]["genero"] == empleados[j]["genero"]:
                    if empleados[i]["nombre"] > empleados[j]["nombre"]:
                        swap_lista(empleados, i, j)
                elif empleados[i]["genero"] > empleados[j]["genero"]:
                    swap_lista(empleados, i, j)
            elif empleados[i]["sector"] > empleados[j]["sector"]:
                    swap_lista(empleados, i, j)

def new_empleado(legajo:str, nombre:str, apellido:str, genero:str, edad:int, email:str, calle:str, localidad:str, provincia:str, sector:str)->dict:
    nuevo_empleado = {}
    nuevo_empleado["legajo"] = legajo
    nuevo_empleado["nombre"] = nombre
    nuevo_empleado["apellido"] = apellido
    nuevo_empleado["genero"] = genero
    nuevo_empleado["edad"] = edad
    nuevo_empleado["email"] = email
    nuevo_empleado["calle"] = calle
    nuevo_empleado["localidad"] = localidad
    nuevo_empleado["provincia"] = provincia
    nuevo_empleado["sector"] = sector
    return nuevo_empleado
