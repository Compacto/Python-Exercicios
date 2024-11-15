salario = float(input('Qual é o seu salário?: '))

while salario < 0:
    salario = float(input('-----------------------\n'
                          'Valor digitado inválido!\n'
                          'informe seu salário corretamente: '))

if salario > 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15

print(f'O seu antigo salário era R$ {salario:.2f} e agora ele irá aumentar para: R$ {aumento:.2f}')