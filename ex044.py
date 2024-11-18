valor = float(input('Informe o valor do produto: R$'))

# Solicita o usuário a forma de pagamento
op = int(input('\033[33mQual é a forma de pagamento?\033[m: \n'
               '1 - \033[32mÀ VISTA (EM DINHEIRO)\033[m 10% DE DESCONTO\n'
               '2 - \033[32mÀ VISTA (NO CARTÃO)\033[m 5% DE DESCONTO\n'
               '3 - \033[32m2X\033[m NO CARTÃO (SEM DESCONTO)\n'
               '4 - \033[32m3X\033[m OU MAIS (20% DE JUROS)\n'
               'Selecione uma opção: '))

# Validar se o usuário digitou o intervalo correto
while op < 1 or op > 4:
    op = int(input('\033[31mOPÇÃO INVÁLIDA!\033[m\n'
                   '\033[33mQual é a forma de pagamento?\033[m: \n'
                   '1 - \033[32mÀ VISTA (EM DINHEIRO)\033[m 10% DE DESCONTO\n'
                   '2 - \033[32mÀ VISTA (NO CARTÃO)\033[m 5% DE DESCONTO\n'
                   '3 - \033[32m2X\033[m NO CARTÃO (SEM DESCONTO)\n'
                   '4 - \033[32m3X\033[m OU MAIS (20% DE JUROS)\n'
                   'Selecione uma opção: '))

# Baseado na opção o código calcula o desconto, não da desconto ou acrescenta juros
if op == 1:
    print(f'O valor a ser pago no produto é: \033[32mR$ {valor - (valor * 0.1):.2f}\033[m')
elif op == 2:
    print(f'O valor a ser pago no produto é: \033[32mR$ {valor - (valor * 0.05):.2f}\033[m')
elif op == 3:
    print(f'O valor a ser pago no produto é: \033[32mR$ {valor:.2f}\033[m')
else:
    print(f'O valor a ser pago no produto é: \033[32mR$ {valor + (valor * 0.2):.2f}\033[m')
