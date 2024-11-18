# Lista para armazenar os pesos
pesos = []

# Laço para ler 5 pesos
for i in range(5):
    peso = float(input('Informe o peso: '))
    # Adiciona o peso à lista
    pesos.append(peso)

# Encontrando o maior e menor peso
maior_peso = max(pesos)
menor_peso = min(pesos)

# Exibindo os resultados
print(f'O maior peso é {maior_peso} kg.')
print(f'O menor peso é {menor_peso} kg.')