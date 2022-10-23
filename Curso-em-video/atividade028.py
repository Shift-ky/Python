 #Escreva um programa que faça o computador “pensar” em um número inteiro 
 # entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número 
 # escolhido pelo computador. O programa deverá escrever na tela se o 
 # usuário venceu ou perdeu.

from random import Random
import random


def linha():
    return print('*'*50)

    


linha()
print('JOGO DA ADIVINHAÇÃO'.center(50))
linha()

computador = random.randint(0,5)

print('Já fiz a minha escolha'.center(50))
print('Faça a sua'.center(50))
linha()

jogador = int(input('Digite um nbúmero de 0 a 5: '))

if computador == jogador:
    print('PARABÉNS!!!')
    print('Você ganhou !')
else:
    print('EU GANHEI!!!!')

print('Obrigado Por esse Jogo!')