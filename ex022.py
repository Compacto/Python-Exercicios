nome = str(input('Digite o seu nome: ').strip())

print(f'Segue as informações\n'
      f'Nome com todas as letras maiúsculas: {nome.upper()}\n'
      f'Nome com todas as letras minúsculas: {nome.lower()}\n'
      f'Quantas letras seu nome possuí (sem considerar os espaços): {len(nome.replace(" ", ""))}\n'
      f'Quantas letras tem o primeiro nome: {len(nome.split()[0])}')