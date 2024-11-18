frase = str(input('Informe uma frase: ')).strip().lower()

# Remover espaços e comparar a frase com sua versão invertida
frase_invertida = frase[::-1]

if frase == frase_invertida:
    print(f'A frase "{frase}" é um palíndromo.')
else:
    print(f'A frase "{frase}" não é um palíndromo.')