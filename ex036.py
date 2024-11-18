valor = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
anos = int(input('Em quantos anos você quer pagar? (obs: permitido apenas de 5 a 35 anos): '))

# Válida se os anos estão dentro do intervalo permitido
while anos < 5 or anos > 35:
    anos = int(input('\033[31mO valor informado está incorreto\033[m\n'
                     'Digite em quantos anos você quer pagar (obs: minímo 5 e máximo 35): '))

# Calcula a prestação após validar o número de anos
prestacao = valor / (anos * 12)

# Verifica se a prestação não excede 30% do salário
if prestacao > salario * 0.3:
    print('\033[31mInfelizmente o empréstimo foi negado devido a prestação exceder 30% do seu salário.\033[m')
else:
    print('\033[32mParabéns, seu empréstimo foi aprovado!!\033[m')