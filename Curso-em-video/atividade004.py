#Faça um programa que leia algo pelo teclado e mostre 
# na tela o seu tipo primitivo e todas as informações 
# possíveis sobre ele.

nome = str(input('Digite algo: '))

print(f'O tipo primitivo desse valor é {type(nome)}')
print(f'só tem espaços? {nome.isspace()}')
print(f'É alfabetico? {nome.isalpha()}')
print(f'É um número? {nome.isnumeric()}')
print(f'É alfanumérico? {nome.isalnum()}')
print(f'Está em minúscula? {nome.islower()}')
print(f'Ésta em maiúscula? {nome.isupper()}')
print(f'Éstá captalizado ? {nome.istitle()}')