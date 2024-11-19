import random

numero = int(input('Digite um número de 0 a 10: '))
numComput = random.randint(0, 10)
contador = 0

# Validar entrada inicial
while numero > 10 or numero < 0:
    numero = int(input('-------------------------------\n'
                       'Opção inválida\n'
                       'Digite um número de 0 a 10 novamente: '))

# Loop para verificar acertos
while numero != numComput:
    if numero < 0 or numero > 10:
        numero = int(input('-------------------------------\n'
                           'Opção inválida\n'
                           'Digite um número de 0 a 10 novamente: '))
    else:
        contador += 1
        numero = int(input('-------------------------------\n'
                           'Você errou! :(\n'
                           'Tente novamente: '))

# Quando acertar
contador += 1  # Contar o palpite correto
print('-------------------------------\n'
      'Você acertou o número!\n'
      f'O número sorteado foi {numComput}.\n'
      f'Foram necessários {contador} palpites para vencer!')