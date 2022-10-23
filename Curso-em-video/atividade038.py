#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

if numero1 > numero2:
    print('O primeiro valor é o maior')
elif numero1 < numero2:
    print('O segundo valor é o maior')
else:
    print('Não existe valor maior, os dois são iguais')