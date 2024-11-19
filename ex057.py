sexo = str(input('Informe o sexo [M ou F]: ')).strip().lower()

while sexo != 'm' and sexo != 'f':
    sexo = str(input('OPÇÃO INVÁLIDA!\n'
                     'Informe o sexo [M ou F]: ')).strip().lower()

print(f'A opção escolhida é: {sexo}')