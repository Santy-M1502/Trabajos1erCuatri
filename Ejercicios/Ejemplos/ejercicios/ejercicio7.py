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
    
print(es_multiplo(10, 3))