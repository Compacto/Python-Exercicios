a = float(input('Informe o comprimento da primeira reta: '))
b = float(input('Informe o comprimento da segunda reta: '))
c = float(input('Informe o comprimento da terceira reta: '))

if a == b == c:
    print('O triângulo é \033[32mequilátero\033[m!\n'
          'Todo os lados são iguais.')
elif a == b or b == c or a == c:
    print('O triângulo é \033[32misósceles\033[m!\n'
          'Dois lados do triângulo são iguais.')
else:
    print('O triângulo é \033[32mescaleno\033[m!\n'
          'Todos os lados são diferentes.')