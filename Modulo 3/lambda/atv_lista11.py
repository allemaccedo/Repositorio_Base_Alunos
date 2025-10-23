numeros = [ 5, 10, 20, 40, 80, 160, -200, -300, -150, 1000]
pares = list(map(lambda n: n % 2 == 0, numeros))

print(pares)