valores = []

while True:
    numero = int(input('Informe o número: '))
    valores.append(numero)

    op = input('Quer continuar? [S/N]: ').strip().lower()

    while op != 's' and op != 'n':
        op = input('OPÇÃO INVÁLIDA. Quer continuar? [S/N]: ')

    if op == 'n':
        break

valorespar = []
valoresimpar = []

for num in valores:
    if num % 2 == 0:
        valorespar.append(num)
for num in valores:
    if num % 2 != 0:
        valoresimpar.append(num)

print(f'Lista dos valores digitados: {valores}')
print(f'Lista apenas dos valores pares: {valorespar}')
print(f'Lista apenas dos valores ímpares: {valoresimpar}')