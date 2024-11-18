nome = str(input("Digite seu nome completo: ").strip())

if 'silva' in nome.lower().split():
    print('Você possuí "Silva" no nome.')
else:
    print('Você não possuí "Silva" no nome.')