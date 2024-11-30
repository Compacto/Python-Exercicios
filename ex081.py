valores = []
cont = 0

while True:
    valores.append(int(input('Digite um valor: ')))
    cont += 1

    op = input('Quer continuar? [S/N]: ').strip().lower()

    while op != 's' and op != 'n':
        op = input('OPÇÃO INVÁLIDA! Quer continuar? [S/N]: ')

    if op == 'n':
        break

valores.sort(reverse=True)

if 5 in valores:
    num5 = 'está na lista.'
else:
    num5 = 'não está na lista.'

print('-=' * 30)
print(f'Foram digitados {cont} números.')
print(f'A lista ordenada de forma decrescente é: {valores}')
print(f'O número 5 {num5}')