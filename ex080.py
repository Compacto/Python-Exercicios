valores = []

for v in range(0, 5):
    valores.append(int(input(f'Digite o {v + 1}º número: ')))

# Ordena a lista
valores.sort()

# Exibe a lista ordenada
print(f'Os valores digitados em ordem foram: {valores}')