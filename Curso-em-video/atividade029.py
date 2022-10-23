#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 
# 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar 
# R$7,00 por cada Km acima do limite.

def linha():
    return print('*'*50)


multa = 0

linha()
print('DEPARTAMENTO DE TRÂNSITO'.center(50))
linha()

velocidade = int(input('Digite a sua velocidade: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    
    print('VOCE FOI \033[31mMULTADO\033[m')
    print(f'O VALOR DA MULTA É DE {multa}')
else:
    print('Você não foi \033[32mMULTADO\033[m!!!')


print('Dirija com cuidado!!!')