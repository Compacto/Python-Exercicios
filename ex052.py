numero = int(input('Digite um número: '))
total = 0

# Conta o número de 1 até o número informado
for c in range(1, numero + 1):
    # Se o resto da divisão do número informado for igual a 0
    if numero % c == 0:
        # Pinta a contagem de verde
        print('\033[32m', end=' ')
        # Ele irá acumular +1 na variável
        total += 1
    else:
        # Se não ele apenas quebra a linha e pinta a contagem de vermelha
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')

print(f'\n\033[mO número \033[32m{numero}\033[m foi divisível {total} vezes')

# Se o total acumular 2 (pois só é considerado número primo se o resto da divisão for 0, ou seja, (numero / 1 e numero / numero)
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')