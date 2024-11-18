from math import hypot

catOpost = float(input('Digite o cateto oposto: '))
catAdj = float(input('Digite o cateto adjacente: '))
hipot = hypot(catOpost, catAdj)

print(f'O comprimento da hipotenusa é: {round(hipot)}')