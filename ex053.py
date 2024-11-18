# Lê a frase, coloca tudo em minúsculo e remove os espaços
frase = ''.join(str(input('Informe uma frase: ')).strip().lower().split())

# Lê a frase do inicio ao fim (::) depois lê ao contrário
frase_invertida = frase[::-1]

if frase == frase_invertida:
    print(f'A frase informada é um palíndromo.')
else:
    print(f'A frase informada não é um palíndromo.')