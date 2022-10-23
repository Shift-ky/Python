# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro númeor: '))
numero3 = int(input('Digite outro número: '))

maior = menor = 0

if numero1 < numero2 and numero1 < numero3:
    menor = numero1
elif numero2 < numero1 and numero2 < numero3:
    menor = numero2
else:
    menor = numero3

if numero1 > numero2 and numero1 > numero3:
    maior = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior = numero2
else:
    maior = numero3

print(f'O maior valor digitado foi: {maior} ')
print(f'O menor valaor digitado foi {menor}')