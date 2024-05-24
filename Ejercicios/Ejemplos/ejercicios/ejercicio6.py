def calcular_resto(dividiendo:int, divisor:int)->int:
    return dividiendo - divisor * (dividiendo // divisor)


print(calcular_resto(10, 2))
# a= dividiendo b= divisor c= cociente d= resto
# a/b = d+c
# c*b-a = d