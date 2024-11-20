# Solicita o primeiro número e inicializa as variáveis
num = int(input('Digite um número: '))
cont = 1  # Contador de números digitados
soma = num  # Inicializa a soma com o primeiro número
lista = [num]  # Lista que armazena todos os números digitados

# Loop para continuar pedindo números até o usuário decidir parar
while True:
    # Pergunta ao usuário se quer continuar
    continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()
    # Se o usuário digitar 'n', o loop é interrompido
    if continuar == 'n':
        break
    # Se o usuário digitar 's', o programa continua pedindo números
    num = int(input('Digite um número: '))
    lista.append(num)  # Adiciona o número à lista
    soma += num  # Atualiza a soma, adicionando o número atual
    cont += 1  # Incrementa o contador de números digitados

# Exibe os resultados finais
print(f'Você digitou {cont} números e a média foi {soma / cont:.2f}\n'  # Calcula a média
      f'O maior valor foi {max(lista)} e o menor foi {min(lista)}')  # Encontra o maior e menor valor na lista