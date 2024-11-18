from datetime import datetime

ano = int(input('Informe seu ano de nascimento: '))
# Calculando a idade usando o ano atual pela lib datetime
idade = datetime.now().year - ano

if idade <= 9:
    print(f'Sua idade é \033[32m{idade}\033[m e você está na categoria: \033[32mMIRIM\033[m')
elif 9 < idade <= 14:
    print(f'Sua idade é \033[32m{idade}\033[m e você está na categoria: \033[32mINFANTIL\033[m')
elif 14 < idade <= 19:
    print(f'Sua idade é \033[32m{idade}\033[m e você está na categoria: \033[32mJUNIOR\033[m')
else:
    print(f'Sua idade é \033[32m{idade}\033[m e você está na categoria: \033[32mMASTER\033[m')