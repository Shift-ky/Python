#Escreva um programa para aprovar o empréstimo bancário para a compra 
# de uma casa. Pergunte o valor da casa, o salário do comprador e em 
# quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
#  do salário ou então o empréstimo será negado.
valorCasa = float(input('Digite o valor da casa a ser comprada\n ->R$ '))
salario = float(input('Digite o valor do se salário mensal\n->R$ '))
anos = int(input('Em quantos anos pretende pagar a casa:\n-> '))

valorMaximoPrestacao = salario*0.30

messes = anos * 12

valorParcela = valorCasa / messes

if valorParcela > valorMaximoPrestacao:
    print(f'EMPRESTIMO NEGADO\nPois as parcelas ficaram muito altas \n {messes} vezes de R${valorParcela:.2f}')
else:
    print(f'Empréstimo concebido serão {messes} parcelas de R${valorParcela:.2f}')

print('\nObrigado pela preferência!')