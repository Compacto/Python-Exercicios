frase = str(input('Digite uma frase: ')).upper().strip()

print(f'Dados da frase:\n'
      f'A letra "A" aparece {frase.count("A", 0)} vezes na frase\n'
      f'A letra "A" aparece pela primeira vez na posição {frase.lower().find("a")+1}\n'
      f'A letra "A" aparece pela última vez na posição: {frase.lower().rfind("a")+1}')
