#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Digite a quantidaade de dinheiro você tem na carteira \n->R$ '))

dolar = real / 5.44

print(f'Com R${real} dá para comprar ${dolar:.2f}')
