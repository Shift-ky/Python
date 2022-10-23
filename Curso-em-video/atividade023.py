#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero= int(input("Informe um valor: "))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10

print(f'Unidade {u}')
print(f'Dezena {d}')
print(f'Centena {c}')