a = float(input('Informe o comprimento da primeira reta: '))
b = float(input('Informe o comprimento da segunda reta: '))
c = float(input('Informe o comprimento da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print('---------------------------------------\n'
          'A soma dos 3 valores formam um triângulo.')
else:
    print('---------------------------------------\n'
          'A soma dos 3 valores não formam um triângulo.')