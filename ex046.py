import time

# Faz a contagem regressiva de 10 até 0
for c in range(10, -1, -1):
    print(c)
    # O sistema aguarda 1 seg pra cada print
    time.sleep(1)

# No final da contagem imprime a mensagem na tela
print('\033[031mFeliz ano novo!!\033[m')