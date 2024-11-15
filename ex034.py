salario = float(input('Qual é o seu salário?: '))

while salario < 0:
    salario = float(input('-----------------------\n'
                          'Valor digitado inválido!\n'
                          'informe seu salário corretamente: '))

if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

print(f'O seu salário irá aumentar em: R$ {aumento:.2f}')