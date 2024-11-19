numero = int(input('Informe um número: '))
fatorial = 1  # Inicializa o fatorial como 1 (neutro multiplicativo)

for i in range(1, numero + 1):  # Vai de 1 até o número, inclusive
    fatorial *= i  # Multiplica cada número do intervalo

print(f'O fatorial de {numero}! é: {fatorial}')