valores = []
while True:
    valores.append(int(input('Digite um valor: ')))

    op = input('Quer continuar? [S/N]: ').strip().lower()

    while op != 's' and op != 'n':
        op = input('OPÇÃO INVÁLIDA! Quer continuar? [S/N]: ').strip().lower()

    if op == 'n':
        break
print('-=' * 30)
print(f'Você digitou os valores {valores}')