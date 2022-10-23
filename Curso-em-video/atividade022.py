#Crie um programa que leia o nome completo de uma pessoas e mostre
#-O nome com todas as letras maiusculas e minusculas
#-Quantas letras tem ao todo(sem considerar os espacos)
#-Quantas letras tem o primeiro nome
from itertools import count


nome = str(input('Digite o seu nome: ')).strip()
print(nome)

print(f'Seu nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Seu Nome com todas as letras minúsculas {nome.lower()}')
print(f'Seu nome tem {len(nome)-nome.count(" ")} letras')

separado = nome.split()

print(f'O seu primeiro nome tem {len(separado[0])} letras')

