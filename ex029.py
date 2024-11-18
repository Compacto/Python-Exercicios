veloCarro = int(input('Quantos KM o carro está andando no momento?: '))
excessoVelo = veloCarro - 80

if veloCarro > 80:
    print(f'Você foi multado!\n'
          f'O valor da multa por excesso de velocidade é: R$ {excessoVelo * 7}')
else:
    print('Você não foi multado, parabéns!')