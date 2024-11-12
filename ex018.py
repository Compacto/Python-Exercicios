import math

ang = float(input('Informe o ângulo: '))

rad = math.radians(ang)

sen = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)


print(f'Segue os valores do: \n'
      f'Seno: {sen}\n'
      f'Cosseno: {cos}\n'
      f'Tangente: {tang}')