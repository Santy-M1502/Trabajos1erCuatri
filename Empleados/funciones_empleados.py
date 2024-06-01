from FuncionesListas import *
from random import randint, choice
from data_empleados import *


def calcular_promedio(lista:list)->float:
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("No esta definico el promedio de una lista vacia")
        return totalizar_lista(lista) / cant
    else:
        raise ValueError("Los valores ingresados deben ser enteros")

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
    if isinstance(lista,list):
        legajo_min = 20000
        legajo_max = 30000
        from random import randint
        lista.append(randint(legajo_min, legajo_max))
    else:
        raise ValueError("Eso no es una lista")
    
def cargar_sueldo(lista:list)->None:
    if isinstance(lista, list):
        lista.append(randint(100000, 200000))
    else:
        raise ValueError("Eso no es una lista")

def cargar_empleados(lista:list, cantidad:int):
    if isinstance(lista,list):
        LEGAJO_INICIAL = 20000
        EDAD_MIN = 18
        EDAD_MAX = 65
        next_legajo = LEGAJO_INICIAL
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
            sueldo = randint(100000, 200000)
            email = f"{nombre.lower()}{apellido.lower()}{choice(dominios)}"
            lista.append(new_empleado(legajo, nombre, apellido, genero, edad, email, calle, localidad, provincia, sector, sueldo))
    else:
        raise ValueError("Eso no es una lista")

def mostrar_empleado(un_empleado:dict):
    if isinstance(un_empleado,dict):
        print(f"Legajo: {un_empleado["legajo"]}\nNombre: {un_empleado["nombre"]} {un_empleado["apellido"]}\nGenero: {un_empleado["genero"]}\nEdad: {un_empleado["edad"]:2}\nDireccion: {un_empleado["calle"]} {un_empleado["localidad"]} {un_empleado["provincia"]}\nSector: {un_empleado["sector"]}\nEmail: {un_empleado["email"]}\nSueldo:$ {un_empleado["sueldo"]:.2f}")
    else:
        raise ValueError("No se ingreso ningun diccionario")

def mostrar_empleado_fila(un_empleado: dict):
    print(f"{un_empleado["legajo"]} {un_empleado["nombre"]:<8} {un_empleado["apellido"]:<10} {un_empleado["genero"]} {un_empleado["edad"]:2} {un_empleado["calle"]:<18} {un_empleado["localidad"]:<12} {un_empleado["provincia"]:<12} {un_empleado["sector"]:<12} {un_empleado["email"]:<20} {un_empleado["sueldo"]:8.2f}")

def mostrar_empleados(empleados:list)->None:
    if isinstance(empleados,list):
        cant = len(empleados)
        print("                             ***Lista de empleados***")
        print("  Legajo   Nombre  Apellido      Genero   Edad     Porvincia     Email            Calle         Sector       Localidad   Sueldo")
        print("-----------------------------------------------------------------------------------------------------------------------")
        for i in range(cant):
            mostrar_empleado_fila(empleados[i])
        print()
    else:
        raise ValueError("Eso no es una lista")
        
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


def ordenar_empleados(empleados:list, campo:str, asc:bool = True):
    if isinstance(empleados,list):
        atributo = definir_campo_alumno(campo)
        tam = len(empleados)
        for i in range(tam - 1):
            for j in range(i + 1, tam):
                if empleados[i][atributo] > empleados[j][atributo] if asc else empleados[i][atributo] < empleados[j][atributo]:
                    swap_lista(empleados, i, j)  
    else:
        raise ValueError("No se ingreso ninguna lista") 

def ordenar_empleados_triple_criterio(empleados:list):
    if isinstance(empleados,list):
        tam = len(empleados)
        for i in range(tam-1):
            for j in range ( i+1, tam):
                if empleados[i]["sector"] == empleados[j]["sector"]:
                    if empleados[i]["genero"] == empleados[j]["genero"]:
                        if empleados[i]["legajo"] > empleados[j]["legajo"]:
                            swap_lista(empleados, i, j)
                    elif empleados[i]["genero"] > empleados[j]["genero"]:
                        swap_lista(empleados, i, j)
                elif empleados[i]["sector"] > empleados[j]["sector"]:
                        swap_lista(empleados, i, j)
    else:
        raise ValueError("Eso no es una lista")

def new_empleado(legajo:str, nombre:str, apellido:str, genero:str, edad:int, email:str, calle:str, localidad:str, provincia:str, sector:str, sueldo:str)->dict:
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
    nuevo_empleado["sueldo"] = sueldo
    return nuevo_empleado

def buscar_nombre_por_legajo(lista:list):
    if isinstance(lista,list):
        legajo_ingresado = int(input("Ingrese el legajo del empleado: "))
        punto_0_flag = False
        for i in range(len(lista)):
            if legajo_ingresado == lista[i]["legajo"]:
                print(lista[i]["nombre"])
                punto_0_flag = True 
        if punto_0_flag == False:
            print("No hay empleados con ese legajo")
    else:
        raise ValueError("Eso no es una lista")

def mostrar_nombre_sector(lista:list):
    if isinstance(lista,list):
        for e in range(len(lista)):
            print(f"{lista[e]["nombre"]} - {lista[e]["sector"]}")
    else:
        raise ValueError("Eso no es una lista")

def buscar_nombre_por_sector(lista:list):
    if isinstance(lista,list):
        sector_ingresado = (input("Ingrese el sector del empleado: "))
        punto_0_flag = False
        for i in range(len(lista)):
            if sector_ingresado == lista[i]["sector"]:
                print(lista[i]["nombre"])
                punto_0_flag = True 
        if punto_0_flag == False:
            print("No hay empleados en ese sector")
    else:
        raise ValueError("Eso no es una lista")

def promedio_sueldo_por_sector(lista:list):
    if isinstance(lista,list):
        sector_ingresado = input("Ingrese el sector: ")
        contador_sector = 0
        sumar_sueldos = 0
        for i in range(len(lista)):
            if sector_ingresado == lista[i]["sector"]:
                sumar_sueldos += lista[i]["sueldo"]
                contador_sector += 1
        if contador_sector != 0:
            print(f"Promedio del sector {sector_ingresado} es {sumar_sueldos / contador_sector}")
        else:
            print("No hay empleados de ese sector")
    else:
        raise ValueError("Eso no es una lista")

def empleado_sector_mayor_sueldo(lista:list):
    if isinstance(lista,list):
        mayor_empleado = None
        mayor_sueldo = None
        mayor_flag = True
        for i in range(len(lista)):
            if mayor_flag == True or lista[i]["sueldo"] > mayor_sueldo:
                mayor_empleado = lista[i]["nombre"]
                mayor_sueldo = lista[i]["sueldo"]
                mayor_flag = False
        print(f"{mayor_empleado} y {mayor_sueldo}")
    else:
        raise ValueError("Eso no es una lista")
    
def empleado_email_corto(lista:list):
    if isinstance(lista,list):
        empleado_corto = []
        flag_corto = True
        for i in range(len(lista)):
            if flag_corto == True or ((lista[i]["email"]) < ([empleado_corto])):
                empleado_corto = []
                flag_corto == False
                empleado_corto.append(lista[i]["email"]) 
            elif (lista[i]["email"] == (empleado_corto)):
                empleado_corto.append(lista[i]["email"])
            print(lista[i]["email"])
            print(empleado_corto)
        
        print(empleado_corto)
    else:
        raise ValueError("Eso no es una lista")

def sector_mas_cobra(lista:list):
    if isinstance(lista,list):
        mayor_sector = None
        mayor_sueldo = None
        mayor_flag = True
        for i in range(len(lista)):
            if mayor_flag == True or lista[i]["sueldo"] > mayor_sueldo:
                mayor_sector = lista[i]["sector"]
                mayor_sueldo = lista[i]["sueldo"]
                mayor_flag = False
        print(f"{mayor_sector} y {mayor_sueldo}")
    else:
        raise ValueError("Eso no es una lista")

def busqueda_binaria_empleado_legajo(legajo, lista):
    inf = 0
    sup = len(lista) - 1
    while inf <= sup:
        medio = (inf + sup) // 2
        if lista[medio]["legajo"] == legajo:
            return medio
        elif legajo > lista[medio]["legajo"]:
            inf = medio + 1
        else:
            sup = medio - 1
    raise ValueError(f"{legajo} is not in list")

def bustar_empleado_legajo(legajo,lista):
    indice = 0
    while indice < len(lista) and lista[indice]["legajo"] != legajo:
        indice += 1
    if indice == len(lista):
        return None
    else:
        return indice

def mapear_nombre_sector(lista:list)->list:
    lista_retorno = []
    for el in lista:
        lista_retorno.append((el["nombre"], el["sector"]))
    return lista_retorno

def mapear_edades(lista:list)->list:
    lista_retorno = []
    for el in lista:
        lista_retorno.append(el["edad"])
    return lista_retorno

def mapear_campo(lista:list, campo)->list:
    lista_retorno = []
    for el in lista:
        lista_retorno.append(el[campo])
    return lista_retorno




def filtar_empleados_sector(lista:list, sector)->list:
    lista_retorno = []
    for el in lista:
        if el["sector"] == sector:
            lista_retorno.append(el)
    return lista_retorno







