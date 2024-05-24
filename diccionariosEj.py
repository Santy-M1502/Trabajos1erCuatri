


un_alumno = {
    "legajo" : 23343,
    "nombre" : "santy",
    "genero" : "masculino",
    "notaP1" : 8,
    "notaP2" : 7,
    "direccion" : {"calle" : "Belgrano 200", "localidad" : "Avellaneda", "provincia" : "BsAs"} 
}

otro_alumno = {
    "legajo" : 32423,
    "nombre" : "maty",
    "genero" : "masculino",
    "notaP1" : 4,
    "notaP2" : 10,
    "direccion" : {"calle" : "Frias 5000", "localidad" : "San Jose", "provincia" : "BsAs"} 
}

for e in un_alumno.keys():#muestra las claves del diccionario
    print(e)

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")

for e in un_alumno.values():#muestra los valores del diccionario
    print(e)

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")

for e in un_alumno.keys():
    print(e, un_alumno[e])

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")

for item in un_alumno.items():#devuelve claves y valores en tuplas
    print(item)

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")

# keys = un_alumno.keys()
keys = list(un_alumno.keys())

print(keys[0])

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")

for clave, valor in un_alumno.items():
    print(clave)
    print(valor)

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")

print(un_alumno["direccion"]["localidad"])

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")

alumnos = []
alumnos.append(un_alumno)
alumnos.append(otro_alumno)

print(alumnos[1]["direccion"]["provincia"])

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")

for alumno in alumnos:
    print(alumno.get("direccion"))

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")

print(un_alumno.pop("nombre"))
print(un_alumno)

print("--.-.---.--.--.-.-.-.-.-.-.-.-.-.-.-.-.-")

print(un_alumno.popitem())
print(un_alumno)




