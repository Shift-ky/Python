#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o valor do seu salário: '))

salario_desconto = salario * 1.15

print(f'O seu salário com o acrécimo de 15% fica {salario_desconto:.2f}')