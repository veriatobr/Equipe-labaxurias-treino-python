'''
    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
'''

Largura = float(input("Digite a Largura desejada: "))
altura = float (input("Digite a Altura desejada: "))
metro4 = altura*Largura
area = metro4
tinta = 2*2 #conversao para metragem total
#sabendo que 1litro pinta 4metros
#sabendo que 1litro pinta 2 metros quadrados
litrom4 = 2
total = area/litrom4

print(f"Eu tenho {area:.0f} Metros quadrados")
print(f"Entao eu preciso de {total:.1f} litros de tinta")