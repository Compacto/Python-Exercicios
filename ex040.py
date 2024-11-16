nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Sua nota é {media} e você foi \033[31mreprovado\033[m.')
elif 5 < media < 7:
    print(f'Sua nota é {media} e você está em \033[33mrecuperação\033[m.')
else:
    print(f'Sua nota é {media} e você foi \033[32maprovado!\033[m.')
