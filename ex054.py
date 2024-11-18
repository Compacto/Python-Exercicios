from datetime import datetime
# Cria as váriaveis para receber os menores/maiores de idade
menores = 0
maiores = 0

# O for conta (c) até 7
for i in range(1, 8):
    # Pede o ano de nascimento e faz o calculo pra revelar a idade
    ano = int(input(f'Informe o ano de {i}ª pessoa nascimento: '))
    idade = datetime.now().year - ano
    # Se a pessoa for menor de idade, incrementa a váriavel menores, se não, incrementa a maiores
    if idade < 18:
        menores = menores + 1
    else:
        maiores = maiores + 1

# Mostra na tela as quantidades de menores e maiores de idade
print(f'Das pessoas digitadas, {menores} não atingiram a maior idade e {maiores} são maiores de idade.')