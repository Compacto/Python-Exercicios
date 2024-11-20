# Solicita ao usuário o primeiro termo da progressão aritmética (PA)
primeiro = int(input('Informe o primeiro número: '))

# Solicita ao usuário a razão da PA (diferença entre os termos consecutivos)
razao = int(input('Informe o segundo número: '))

# Pergunta ao usuário quantos termos ele quer exibir inicialmente
cont = int(input('Quantos termos você quer mostrar?: '))

# Inicializa a variável 'termo' com o valor do primeiro termo da PA
termo = primeiro

# Reinicia o contador para acompanhar os termos exibidos
cont = 1

# Inicializa o total de termos exibidos como 0
total = 0

# Inicializa a variável 'mais' com 10, indicando que serão exibidos 10 termos adicionais por padrão
mais = 10

# Enquanto o usuário não solicitar 0 termos adicionais, o loop continua
while mais != 0:
    # Soma os termos adicionais solicitados ao total de termos a exibir
    total = total + mais

    # Loop interno para exibir os termos da PA até alcançar o total desejado
    while cont <= total:
        # Exibe o termo atual da PA seguido de uma seta
        print(f'{termo} -> ', end='')

        # Incrementa o termo com base na razão da PA
        termo += razao

        # Incrementa o contador para registrar que um termo foi exibido
        cont += 1

    # Indica uma pausa no programa para decidir se o usuário quer continuar
    print('PAUSA')

    # Pergunta ao usuário quantos termos adicionais ele quer exibir
    mais = int(input('Quantos mais termos você quer mostrar?: '))

# Mensagem final ao encerrar o programa
print('Obrigado por usar o software, até breve!')