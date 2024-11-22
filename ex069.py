cont_idade = 0
mulher_menos20 = 0
homens = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)

    # Entrada e validação para idade
    idade = int(input('Idade: '))

    # Entrada e validação para sexo
    sexo = input('Sexo: [M/F]: ').strip().lower()
    while sexo not in ('m', 'f'):
        print('Entrada inválida! Digite "M" para masculino ou "F" para feminino.')
        sexo = input('Sexo: [M/F]: ').strip().lower()

    # Contagem de condições
    if idade >= 18:
        cont_idade += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulher_menos20 += 1

    # Opção de continuar
    print('-' * 30)
    op = input('Quer continuar? [S/N]: ').strip().lower()
    while op not in ('s', 'n'):
        print('Entrada inválida! Digite "S" para sim ou "N" para não.')
        op = input('Quer continuar? [S/N]: ').strip().lower()

    if op == 'n':
        break

# Saída final
print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {cont_idade}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulher_menos20} mulher(es) com menos de 20 anos.')