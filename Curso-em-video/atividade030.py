#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print('O número informado é PAR')
else:
    print('O número informado é ÍMPAR')