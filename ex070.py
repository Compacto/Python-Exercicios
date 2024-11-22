produtos_1000 = 0
total_compra = 0
produto_mais_barato = None
valor_mais_barato = float('inf')  # Um valor muito alto para comparação inicial

print('-' * 30)
print('      LOJA SUPER BARATÃO')
print('-' * 30)

while True:
    nome = input('Nome do produto: ')
    valor = float(input('Preço: R$'))

    # Adicionando o valor do produto ao total da compra
    total_compra += valor

    # Verificando se o produto custa mais de 1000
    if valor > 1000:
        produtos_1000 += 1

    # Verificando se esse é o produto mais barato
    if valor < valor_mais_barato:
        produto_mais_barato = nome
        valor_mais_barato = valor

    # Opção de continuar
    print('-' * 30)
    op = input('Quer continuar? [S/N]: ').strip().lower()

    while op not in ('s', 'n'):
        print('Entrada inválida! Digite "S" para sim ou "N" para não.')
        op = input('Quer continuar? [S/N]: ').strip().lower()

    if op == 'n':
        break

print('-' * 15, ' FIM DO PROGRAMA ', '-' * 15)
print(f'O total da compra foi R${total_compra:.2f}')
print(f'Temos {produtos_1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi "{produto_mais_barato}" que custa R${valor_mais_barato:.2f}')