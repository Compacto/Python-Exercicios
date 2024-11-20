termo = int(input('Informe o termo: '))
razao = int(input('Informe a razao: '))
termo = int(termo)
cont = 1

while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')