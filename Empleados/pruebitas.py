from funciones_empleados import mapear_lista

def duplicar(a):
    return a * 2

def mitad(a):
    return a // 2

def pasar_mayusculas(cadena):
    return cadena.upper()

unaFuncion = pasar_mayusculas

numeros = [3, 45,2, 3, 66, 4, 5, 56, 456]

nombres = ["Juan", "María",  "Ricardo", "Julia", "Joaquín", "Cristina", "Antonio", "Lorena", "Manuel", "Virginia"]

x = mapear_lista(unaFuncion, nombres)

print(x)
