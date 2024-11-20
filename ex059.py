from time import sleep

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))

menu = 0  # Inicializa o menu
while menu != 5:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
          'INFORME A OPÇÃO DESEJADA')
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')

    menu = int(input('Sua escolha: '))

    # Validar a opção do menu
    while menu < 1 or menu > 5:
        menu = int(input('OPÇÃO INVÁLIDA!\n'
                         'Escolha novamente: '))

    # Executar a ação escolhida
    if menu == 1:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
              f'A soma de {num1} e {num2} é: {num1 + num2}\n'
              f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        sleep(1)
    elif menu == 2:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
              f'A multiplicação de {num1} e {num2} é: {num1 * num2}\n'
              f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        sleep(1)
    elif menu == 3:
        maior = max(num1, num2)
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
              f'O maior número é: {maior}\n'
              f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        sleep(1)
    elif menu == 4:
        # Solicitar novos números
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
              'Informe novos números...')
        num1 = float(input('Informe o primeiro número: '))
        num2 = float(input('Informe o segundo número: '))
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        sleep(1)
    elif menu == 5:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
              'Obrigado por utilizar o software. Até breve!\n'
              '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')