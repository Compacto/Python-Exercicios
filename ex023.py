numero = int(input('Informe um número entre 0 e 9999: '))

while numero < 0 or numero > 9999:
    numero = int(input('Digite um número válido entre 0 e 9999: '))


print(f'Segue os dados do número: \n'
        f'Unidade: {numero % 10}\n'
        f'Dezena: {(numero // 10) % 10}\n'
        f'Centena: {(numero // 100) % 10}\n'
        f'Milhar: {(numero // 1000) % 10}')