#Escreva um programa em Python que leia um número inteiro qualquer e 
# peça para o usuário escolher qual será a base de conversão: 1 para binário,
#  2 para octal e 3 para hexadecimal.
numero = int(input('Digite um valor: '))

print('''[1] - BINARIO
[2] - OCTAL
[3] - HEXADECIMAL''')
opc =(int(input('-> ')))

if opc ==1:
    print(f'O valor em Binário é {bin(numero)[2:]}')
elif opc == 2:
    print(f'O valor em Octal é {oct(numero)[2:]}')
elif opc == 3:
    print(f'O valor em Hexadecimal é {hex(numero)[2:]}')
