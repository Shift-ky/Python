#Exercício Python 041: A Confederação Nacional de Natação 
# precisa de um programa que leia o ano de nascimento de um 
# atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import datetime


anoNascimento = int(input('Digite o ano de nascimento do atleta: '))

anoAtual = datetime.today().year

idade = anoAtual - anoNascimento

if idade <= 9:
    print('Selecionado na categoria \033[32mMIRIN\033[m')
elif idade <= 14:
    print('Selecionado na categoria \033[32mINFANTIL\033[m')
elif idade <= 19:
    print('Selecionado na categoria \033[32mJÚNIOR\033[m')
elif idade <= 25:
    print('Selecionado na categoria \033[32mSÊNIOR\033[m')
else:
    print('Selecionado na categoria \033[32mMASTER\033[m')