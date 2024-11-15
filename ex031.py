distancia = int(input('Informe a distância da viagem em KM: '))

while distancia < 0:
    distancia = int(input('-----------------------\n'
                          'Valor digitado inválido!\n'
                          'Informe a distância da viagem em KM: '))

if distancia > 0 and distancia <= 200:
    print(f'------------------------------------\n'
          f'O valor da passagem é: R$ {distancia * 0.50:.2f}')
else:
    print(f'------------------------------------\n'
          f'O valor da passagem é: R$ {distancia * 0.45:.2f}')
