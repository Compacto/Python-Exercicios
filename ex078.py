numeros = []

for c in range(1, 6):
    numeros.append(int(input(f'Digite o {c}º número: ')))

print(f'Você digitou os valores {numeros}')

maior = max(numeros)
menor = min(numeros)

print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(i + 1, end=' ')

print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(i + 1, end='')