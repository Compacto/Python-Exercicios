soma = 0

for c in range(1, 7):
    numero = int(input(f'Informe o {c}º número: '))
    # Calculo de verificação do número par
    if numero % 2 == 0:
        soma += numero

print(f'A soma dos números informados apenas considerando os números pares é: {soma}')