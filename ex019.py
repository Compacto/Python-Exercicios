import random

alun1 = (input('Informe o nome do primeiro aluno: '))
alun2 = (input('Informe o nome do segundo aluno: '))
alun3 = (input('Informe o nome do terceiro aluno: '))
alun4 = (input('Informe o nome do quarto aluno: '))

lista = [alun1, alun2, alun3, alun4]

print(f'O aluno escolhido foi: {random.choice(lista)}')