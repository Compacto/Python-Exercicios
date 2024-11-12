from math import sin, cos, tan, radians

ang = float(input('Informe o ângulo: '))

rad = radians(ang)

sen = sin(rad)
cos = cos(rad)
tang = tan(rad)


print(f'Segue os valores do: \n'
      f'Seno: {sen}\n'
      f'Cosseno: {cos}\n'
      f'Tangente: {tang}')