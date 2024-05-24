def duplicar(valor:int) ->int:
    """_summary_

    Args:
        valor (int): numero a duplicar

    Returns:
        int: retorna el doble del numero ingresado
    """
    return valor * 2

def calcular_resto(dividiendo:int, divisor:int)->int:
    return dividiendo - divisor * (dividiendo // divisor)

def es_multiplo(a:int, b:int)-> bool:
    """verifica si es un numero es multiplo de otro

    Args:
        a (int): numero a verificar
        b (int): posible multiplo

    Returns:
        bool: retorna True si b es multiplo de a, False en caso contrario
    """
    # if (a % b) == 0:
    #     return True
    # else:
    #     return False
    return b % a == 0

def calcular_perimeto_circuferencia(radio: int)->float:
    from math import pi
    return 2 * radio * pi


def sorteador(lista:list)->None:
    from random import randint
    if isinstance(lista,list):
        import time
        i = randint(0, len(lista) - 1)
        time.sleep(3)
        print(f"The winner is ----->{ lista[i]}")
    else:
        raise TypeError("No es una lista")
    

lista = ["Martinez", "Ortiz", "Nieva", "Quiroga", "Lopez", "Mariani", "Perotto", "BDemon", "Baus", "Santana", "Mingorance", "Quipildor", "Mansilla", "Morales", "Quiroga", "Perez", "Rodriguez", "Llusa", "Moro", "Bustelo", "Lopez", "Lukkv", "Poloni", "Rodriguez", "Nuñez", "Rivadeneira", "Moyano", "Lubrano", "Navarro", "Maldonado", "Rios", "Brenda", "Ponce", "Pucheta", "Puricelli", "Pardox", "Luna", "Melsa", "Pages"]
(sorteador(lista))