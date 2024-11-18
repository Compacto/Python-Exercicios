import time
import sys
from random import shuffle

# Função "novo jogo"
def jogar():
    while True:
        # Recebe a escolha do usuário:
        op = int(input('Vamos jogar jokenpô?!\n'
                       'Escolha uma das opções abaixo!:\n'
                       '1 - \033[1;33mPedra\033[m\n'
                       '2 - \033[1;32mPapel\033[m\n'
                       '3 - \033[1;34mTesoura\033[m\n'
                       'Opção: '))

        # Verifica se a opção está dentro do intervalo
        while op < 1 or op > 3:
            op = int(input('\033[1;31mOPÇÃO INVÁLIDA!\033[m\n'
                           'Escolha uma das opções abaixo!:\n'
                           '1 - \033[1;33mPedra\033[m\n'
                           '2 - \033[1;32mPapel\033[m\n'
                           '3 - \033[1;34mTesoura\033[m\n'
                           'Opção: '))

        # O computador escolhe a opção que ele deseja usando um shuffle
        lista = [1, 2, 3]
        shuffle(lista)

        # Apenas uma animação que mostra "Carregando..." para mostrar de forma lúdica que o computador também está jogando
        def loading_animation():
            for i in range(6):  # Define o número de repetições do ciclo de animação
                sys.stdout.write(
                    '\r\033[1;32mDeixe-me pensar' + '.\033[m' * (i % 3 + 1))  # Exibe a animação com 1, 2 ou 3 pontos
                sys.stdout.flush()  # Limpa a linha anterior
                time.sleep(0.5)  # Intervalo entre as animações

        # Carrega a animação para ser mostrada
        loading_animation()

        # Baseado nas escolhas do jogador e do computador, é feita uma comparação do resultado (o \n no inicio do print é para quebrar a linha entre o "Carregando...")
        if op == lista[0]:
            print(f'\nEu escolhi \033[1;33mPedra\033[m!\n'
                  '\033[1;32mEmpatamos :( \033[m\n'
                  '\033[1;32mTente novamente!\033[m')
        elif op == 1 and lista[0] == 2:
            print('\nEu escolhi \033[1;32mPapel\033[m!\n'
                  'Você perdeu! \033[1;31mPapel cobre Pedra\033[m')
        elif op == 1 and lista[0] == 3:
            print('\nEu escolhi \033[1;34mTesoura\033[m!\n'
                  'Você ganhou! \033[1;33mPedra quebra Tesoura\033[m')

        elif op == 2 and lista[0] == 1:
            print('\nEu escolhi \033[1;33mPedra\033[m!\n'
                  'Você ganhou! \033[1;32mPapel cobre Pedra\033[m')
        elif op == 2 and lista[0] == 3:
            print('\nEu escolhi \033[1;34mTesoura\033[m!\n'
                  'Você perdeu! \033[1;32mTesoura corta Papel\033[m')

        elif op == 3 and lista[0] == 1:
            print('\nEu escolhi \033[1;33mPedra\033[m!\n'
                  'Você perdeu! \033[1;31mPedra quebra Tesoura\033[m')
        elif op == 3 and lista[0] == 2:
            print('\nEu escolhi \033[1;32mPapel\033[m!\n'
                  'Você ganhou! \033[1;34mTesoura corta Papel\033[m')

        # Perguntar se o usuário deseja jogar novamente
        jogar_novamente = str(input('\nDeseja jogar novamente? (\033[32ms\033[m/\033[31mn\033[m): ')).strip().lower()
        if jogar_novamente == 's':
            continue  # Faz com que o programa pule o resto do if e vá direto pra proxima interação ("jogar()")
        else:
            print('\033[34mObrigado por jogar!\033[m')
            break
# Inicia o jogo
jogar()