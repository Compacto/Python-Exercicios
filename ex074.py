from random import randint
sorteio = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Os valores sorteados foram: {sorteio}')
print(f'O maior valor do sorteio é {max(sorteio)} e o menor valor é {min(sorteio)}')