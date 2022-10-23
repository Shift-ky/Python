#Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros
valorProduto = float(input('Digite o valor do produto: '))

print('''[1] - À vista
[2] - Débito
[3] - crédito 2X
[4] - crédito 3x ou mais''')
opc = int(input('-> '))

if opc == 1:
    valorPagar = valorProduto*0.90
    print(f'Valor a pagar: R${valorPagar:.2f}')
    print(f'Desconto R${valorProduto-valorPagar:.2f}')

elif opc == 2:
    valorPagar = valorProduto*0.95
    print(f'Valor a pagar: R${valorPagar:.2f}')
    print(f'Desconto R${valorProduto - valorPagar:.2f}')
    
elif opc == 3:
    print(f'Valor a pagar: R${valorProduto:.2f}')
    print(f' {2} parcelas de R${valorProduto/2:.2f}')

elif opc == 4:
    valorPagar = valorProduto * 1.20
    
    opc = int(input('3x\n4x\n5x\n6x\n7x\n8x\n9x\n10x\n -> '))

    print(f'Valor a ser pago R${valorPagar:.2f}')
    print(f' {opc} parcelas de R${valorPagar/opc:.2f}')
else:
    print('opção inválida')
