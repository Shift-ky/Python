#Faça um programa que leia o nome completo de uma pessoa, mostrando 
# em seguida o primeiro e o último nome separadamente.

from posixpath import split


nome = str(input('Digite o seu nome completo: '))

separado = nome.split()

print(f'Primeiro nome: {separado[0]}\nSobrenome: {separado[-1]} ')