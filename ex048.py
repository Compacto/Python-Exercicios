soma = 0  # Variável acumuladora para a soma

# Percorre os números de 1 a 500 e faz a leitura de 2 em 2, pegando somente os números ímpares
for numero in range(1, 501, 2):
    # Adiciona na soma se o número for múltiplo de 3
    if numero % 3 == 0:
        # Soma o número na variável acumuladora
        soma += numero

# Exibe o resultado
print(f"A soma de todos os números ímpares e múltiplos de 3 de 1 a 500 é {soma}.")