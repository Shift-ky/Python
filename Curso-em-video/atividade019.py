#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#  Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na
#  tela o nome do escolhido.

import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.choice(lista)

print(f'O aluno sorteado foi: {sorteado}')
