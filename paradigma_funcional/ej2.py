
def fabrica_funciones(nombre):
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    def operar(operacion, op1, op2):
        return operacion(op1, op2)

    match nombre:
        case "s": return sumar
        case "r": return restar
        case "m": return multiplicar
        case "d": return dividir

a = 20
b = 10

miFuncion = fabrica_funciones("r")
print(miFuncion(a, b))






