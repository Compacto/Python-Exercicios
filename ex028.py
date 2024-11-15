import random
numero = int(input('Digite um número de 0 a 5: '))

numComput = random.randint(0 , 5)

while numero > 5 or numero < 0:
    numero = int(input('-------------------------------\n'
                       'Opção inválida\n'
                       'Digite um número de 0 a 5 novamente: '))


if numero == numComput:
    print(f'-------------------------------\n'
          f'Parabéns, você adivinhou o número sorteado!\n'
          f'O número era: {numComput}')
else:
    print('-------------------------------\n'
          'Você errou o número, tente novamente!')