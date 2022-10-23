#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
#  até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distancia da viagem: '))

valorViagem = 0

if distancia <= 200:
    valorViagem = distancia *0.50
else:
    valorViagem = distancia*0.45

print(f'O valor a ser pago pela su viagem é R${valorViagem:.2f}')
