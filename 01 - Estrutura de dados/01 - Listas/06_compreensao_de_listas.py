# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

"""Seria equivalente a 
for numero in numeros:
    if numero % 2 == 0 
        pares.append(numero)"""

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

"""
Seria equivalente a 
for numero in numeros:
    quadrado.append(numero ** 2)"""