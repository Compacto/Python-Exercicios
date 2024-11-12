nome = input('Digite o seu nome completo: ').strip()

print(f'Dados do nome digitado: \n'
      f'O seu primeiro nome é: {nome.split()[0]}\n'
      f'Seu último nome é: {nome.split()[-1]}')