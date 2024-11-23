import random

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
cont = 0

while True:
    valor = int(input('Digite um valor: '))
    op = str(input('Par ou Ímpar? [P/I]: ')).strip().lower()

    while op not in ('p', 'i'):
        op = input('Escolha inválida! Par ou Ímpar? [P/I]: ').strip().lower()

    aleatorio = random.randint(1, 10)
    soma = valor + aleatorio

    if soma % 2 == 0 and op == 'p':
        print('-' * 20)
        print(f'Você jogou {valor} e o computador {aleatorio}. Total de {soma} DEU PAR')
        print('-' * 20)
        print('Você VENCEU!\n'
              'Vamos jogar novamente...')
        print('=-' * 20)
        cont += 1
    elif soma % 2 != 0 and op == 'i':
        print('-' * 20)
        print(f'Você jogou {valor} e o computador {aleatorio}. Total de {soma} DEU ÍMPAR')
        print('-' * 20)
        print('Você VENCEU!\n'
              'Vamos jogar novamente...')
        print('=-' * 20)
        cont += 1
    else:
        print('Você PERDEU!')
        break

print(f'GAME OVER! Você venceu {cont} vezes.')





