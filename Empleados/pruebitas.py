from funciones_empleados import mapear_lista, filtrar_lista

def duplicar(a):
    return a * 2

def mitad(a):
    return a // 2

def pasar_mayusculas(cadena):
    return cadena.upper()

unaFuncion = pasar_mayusculas

numeros = [3, 45,2, 3, 66, 4, 5, 56, 456]

nombres = ["Juan", "María",  "Ricardo", "Julia", "Joaquín", "Cristina", "Antonio", "Lorena", "Manuel", "Virginia"]

# x = filtrar_lista(lambda numero:numero > 30 and numero < 60 , numeros)
# x = mapear_lista(lambda nombre: len(nombre), ["Juan", "María", "Ricardo", "Virginia"])
x = filtrar_lista(lambda nombre: len(nombre) < 6, nombres)


print(x)
