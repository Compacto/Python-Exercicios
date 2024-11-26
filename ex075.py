num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))

numeros = (num1, num2, num3, num4)
cont = 0
pares = []

for numero in numeros:
    if numero == 9:
        cont += 1
    if numero % 2 == 0:
        pares.append(numero)

if 3 in numeros:
    posicao_3 = numeros.index(3) + 1
else:
    posicao_3 = 'nenhuma'

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {cont} vezes')
print(f'O valor 3 apareceu {posicao_3}ª posição')
print(f'Os valores pares digitados foram {pares}')