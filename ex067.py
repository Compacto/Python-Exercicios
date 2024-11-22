while True:
    numero = int(input('Quer ver a tabuada de qual valor?: '))

    if numero >= 1:
        print('-----------------------------')
        for i in range(1, 11):  # Loop de 1 a 10
            print(f'{numero} x {i} = {numero * i}')
        print('-----------------------------')
    else:
        break
print('PROGRAMA ENCERRADO')