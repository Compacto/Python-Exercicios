numero = int(input('Digite um número: '))

print(f'Segue a tabuada do número {numero}')
for c in range(0, 11):
    print(f'{numero} x {c} = {numero * c}')
