numeros = [1, 2, 3, 4, 5, 6]
quadrado = lambda x: x * x
quadrados = list(map(quadrado, numeros ))

print(quadrados)