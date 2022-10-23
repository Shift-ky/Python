#Escreva um programa que pergunte o salário de um funcionário e calcule
#  o valor do seu aumento. Para salários superiores a R$1250,00, calcule
#  um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o valor do seu salário: '))

almeto_salario = 0
if salario > 1250:
    almento_salario = salario*1.10
else:
    almento_salario = salario*1.15

print(f'O valor do seu salário passa a ser R${almento_salario:.2f}')