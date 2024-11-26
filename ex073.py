brasileirao_2024 = ("Botafogo", "Palmeiras", "Flamengo", "Atlético-MG", "Grêmio", "Athletico-PR", "Fluminense", "São Paulo", "Fortaleza", "Cruzeiro", "Internacional", "Cuiabá", "Corinthians", "Red Bull Bragantino", "Bahia", "Santos", "Goiás", "Vasco da Gama", "Coritiba", "América-MG")

print(f'Os cinco primeiros colocados são: {brasileirao_2024[0:5]}')
print('-' * 30)
print(f'Os quatro últimos colocados são {brasileirao_2024[-4]}')
print('-' * 30)
print(f'Os colocados em ordem alfabética são: {sorted(brasileirao_2024)}')
print('-' * 30)

for pos, time in enumerate(brasileirao_2024):
    if time == 'Corinthians':
        print(f'O {time} está na {pos + 1}ª posição.')