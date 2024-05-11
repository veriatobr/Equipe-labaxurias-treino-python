'''
     Crie um programa que leia quanto dinheiro em reais uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
'''
carteira = float(input("Eu tenho na carteira R$ "))
dolar = carteira/5.16
print(f"Eu Tenho na Carteira R${carteira:.2f} Reais")
print(f"Eu posso comprar ${dolar:.2f} dolares, com os R${carteira:.2f}Reais que tenho na carteira")

