#Faça um programa que leia o comprimento do cateto oposto e do cateto 
# adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

cateto_oposto = float(input('Digite o valo do cateto opoosto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2)

print(f'O valor da hipotenusa é {hipotenusa}')