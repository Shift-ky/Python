#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cid = str(input('Digite o nome da cidade: '))

print(cid[:5].upper() == 'SANTO')
