numero = int(input('Informe um número inteiro: '))
base = int(input('Escolha uma das opções: \n'
                 '1 - Binário\n'
                 '2 - Octal\n'
                 '3 - hexadecimal\n'
                 'Opção: '))

# Validação da opção escolhida
while base < 1 or base > 3:
    base = int(input('\033[31mOpção inválida!\033[m\n'
                     'Escolha uma das opções: \n'
                     '1 - Binário\n'
                     '2 - Octal\n'
                     '3 - hexadecimal\n'
                     'Opção: '))

# Efetuando as condições e convertendo baseada na opção desejada
if base == 1:
    print(f'O número {numero} convertido para binário é: \033[32m{bin(numero)[2:]}\033[m')
elif base == 2:
    print(f'O número {numero} convertido para octal é: \033[32m{oct(numero)[2:]}\033[m')
else:
    print(f'O número {numero} convertido para hexadecimal é: \033[32m{hex(numero)[2:]}\033[m')