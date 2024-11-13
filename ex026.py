frase = str(input('Digite uma frase: '))

print(f'Dados da frase:\n'
      f'A letra "A" aparece {frase.count("a", 0)} vezes na frase\n'
      f'A letra "A" aparece pela primeira vez na posição {frase.lower().find("a")}\n'
      f'A letra "A" aparece pela última vez na posição: {frase.lower().rfind("a")}')
