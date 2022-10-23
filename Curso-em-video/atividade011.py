#Faça um programa que leia a largura e a altura de uma parede em metros,
#  calcule a sua área e a quantidade de tinta necessária para pintá-la,
#  sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da parede '))
altura = float(input('Digite a altura da parede'))

metros2 = largura*altura

tintaL = metros2/2

print(f'Uma parede de {largura}X{altura} vai precisar de {tintaL} litros de tintas.')