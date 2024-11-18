somaidade = 0
maioridadehomem = 0
mediaidade = 0
nomevelho = ''
totalmulher20 = 0

for i in range(1, 5):
    print(f'--------- {i}ª PESSOA ---------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    somaidade += idade

    while sexo != 'm' and sexo != 'f':
        sexo = str(input('OPÇÃO INVÁLIDA!\n'
                         'Sexo [M/F]: ')).strip().lower()

    # Verificando o homem mais velho
    if sexo == 'm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    # Contabilizando mulheres com menos de 20 anos
    if sexo == 'f' and idade < 20:
        totalmulher20 += 1

# Calculando a média de idade
mediaidade = somaidade / 4

print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totalmulher20} mulheres com menos de 20 anos.')