itens = (("Camiseta", 50.0), ("Calça", 120.0), ("Tênis", 200.0))

print('-' * 50)
print('                LISTAGEM DE PREÇOS                    ')
print('-' * 50)

for item, preco in itens:
    print(f'O preço do {item} é R${preco}')

print('-' * 50)