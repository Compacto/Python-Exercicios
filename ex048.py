soma = 0  # Variável acumuladora para a soma

# Percorre os números de 1 a 500
for numero in range(1, 501):
    # Verifica se o número é ímpar e múltiplo de 3
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero  # Soma o número na variável acumuladora

# Exibe o resultado
print(f"A soma de todos os números ímpares e múltiplos de 3 de 1 a 500 é {soma}.")