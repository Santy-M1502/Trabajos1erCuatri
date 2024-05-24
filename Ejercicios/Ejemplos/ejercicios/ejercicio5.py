

def duplicar(valor:int) ->int:
    """_summary_

    Args:
        valor (int): numero a duplicar

    Returns:
        int: retorna el doble del numero ingresado
    """
    return valor * 2

#testing(probar)
num1 = int(input("Ingrese un numero "))

print(f"el doble es: {duplicar(num1)}")