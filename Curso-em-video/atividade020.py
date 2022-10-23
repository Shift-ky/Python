# O mesmo professor do desafio 19 quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro
# alunos e mostre a ordem sorteada.
import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

print('A ordem de apresentação será')
print(sorted(lista))
