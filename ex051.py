termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

# Calcular os 10 primeiros termos
for c in range(10):
    # Formula da progressão aritmética
    posicao = termo + c * razao
    # Exibe os 10 primeiros termos e um "end" pra ficar tudo na mesma linha
    print(posicao, end=' -> ')
print('FIM')