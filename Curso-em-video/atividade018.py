#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o valor de um angulo:'))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print(f'Valor do seno {sen:.2f}')
print(f'Valor do coseno {cos:.2f}')
print(f'Valor da tangente {tang:.2f}')