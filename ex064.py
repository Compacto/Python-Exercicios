num = 0
soma = 0
numDigitados = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma += num
    numDigitados += 1

print(f'Você digitou {numDigitados - 1} números e a soma entre eles é {soma - 999}')