cont = 0
soma = 0

while True:
    numero = int(input('Informe um número (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')