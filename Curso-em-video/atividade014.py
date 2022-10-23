#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

graus = float(input('Digite a temperatura: '))

fahrenheint = (graus * (9/5)) + 32

print(f'{graus} em fahrenheit é {fahrenheint}')