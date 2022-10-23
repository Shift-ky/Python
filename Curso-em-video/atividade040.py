#Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))

media = (nota1 + nota2 + nota3)/3

if media < 5.0:
    print('O aluno está\033[31m REPROVADO\033[m!!!')
elif media < 6.9:
    print('O aluno está de \033[33mRECUPERAÇÃO\033[m!!!')
else:
    print('O aluno está \033[32mAPROVADO\033[m!!!')