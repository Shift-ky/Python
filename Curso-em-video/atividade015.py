# Escreva um programa que pergunte a quantidade de Km percorridos por um carro
#  alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço 
# a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos kilometros rodados: '))
dia = int(input('Quantos dias passou com o carro: '))

valor_dia = dia * 60
valor_km = km * 0.15

print(f'O valor a ser apago pelo carro é R${valor_km+valor_dia:.2f}')