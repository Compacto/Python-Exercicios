soma = 0

for c in range(0, 6):
    numero = int(input('Informe um número: '))
    if numero % 2 == 0:
        soma += numero

print(f'A soma dos números informados apenas considerando os números pares é: {soma}')
