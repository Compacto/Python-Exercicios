# Condição para testar se o usuário está inserindo números inteiros
while True:
    try:
        num1 = int(input('Informe o primeiro número inteiro: '))
        break  # Sai do loop se a entrada for válida
    except ValueError:
        print('\033[31mErro: Por favor, insira apenas números inteiros.\033[m')

while True:
    try:
        num2 = int(input('Informe o segundo número inteiro: '))
        break  # Sai do loop se a entrada for válida
    except ValueError:
        print('\033[31mErro: Por favor, insira apenas números inteiros.\033[m')


# Condicional para organizar os números entre qual é maior, caso contrário é igual.
if num1 > num2:
    print(f'\033[32m{num1}\033[m é maior que \033[31m{num2}\033[m.')
elif num2 > num1:
    print(f'\033[32m{num2}\033[m é maior que \033[31m{num1}\033[m.')
else:
    print(f'O número \033[32m{num1}\033[m e \033[32m{num2}\033[m são iguais.')