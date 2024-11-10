diasAlug = int(input('Por quantos dias o carro foi alugado?: '))
kmRod = int(input('Quantos KM você rodou com o carro?: '))
print(f'O total a pagar é: R${(kmRod * 0.15) + (diasAlug * 60)}')