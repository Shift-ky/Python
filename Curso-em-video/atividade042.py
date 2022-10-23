#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar 
# que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

reta1 = float(input('Digite o valor da primera reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Essas três retas forma um triângulo')

    if reta1 == reta2 and reta1 == reta3:
        print('EQUILÁTERO')
    elif reta1 != reta2 and reta1 != reta3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Essas três retas não forman um triângulo')