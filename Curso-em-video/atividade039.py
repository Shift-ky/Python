#Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço 
# militar, se é a hora exata de se alistar ou se já passou do tempo 
# do alistamento. Seu programa também deverá mostrar o tempo que falta 
# ou que passou do prazo.
from datetime import datetime

atual = datetime.today().year

anoNascimento = int(input('Digite o seu ano de nascimento: '))

idade = atual - anoNascimento;

if idade == 18:
    print('\033[33mALERTA\033[m'.center(50))
    print('VOCÊ ESTÁ NA IDADE CERTA PARA SE ALISTAR'.center(50))
elif idade < 18:
    print('ainda não chegou o tempo do seu alistamento')
    print(f'ainda falta {18 - idade} anos para o seu alistamento')
else:
    print('Já passou da data do seu alistamento')
    print(f'Já se passaram {idade - 18} anos do seu alistamento')    
