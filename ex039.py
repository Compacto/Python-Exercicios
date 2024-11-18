from datetime import datetime

ano = int(input('Informe o seu ano de nascimento: '))

# Calcula a idade baseada no ano de nascimento
idade = datetime.now().year - ano

# Verifica a aptidão ao alistamento militar
if idade == 18:
    print('\033[32mVocê está apto para se alistar no serviço militar!\033[m')
elif idade < 18:
    print(f'Você ainda não pode se alistar no serviço militar, pois faltam \033[33m{18 - idade}\033[m ano(s) para a idade necessária!')
else:
    print(f'Você passou \033[31m{idade - 18}\033[m ano(s) da data do alistamento militar!')