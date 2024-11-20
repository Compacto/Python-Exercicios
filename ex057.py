sexo = str(input('Informe o seu sexo [M ou F]: ')).strip().lower()

while sexo != 'm' and sexo != 'f':
    sexo = str(input('OPÇÃO INVÁLIDA!\n'
                     'Por favor, informe o seu sexo [M ou F]: ')).strip().lower()

if sexo == 'm':
    print('A seu sexo é: feminino')
else:
    print('Seu sexo é: masculino')