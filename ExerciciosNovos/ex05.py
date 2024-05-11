'''
    Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
'''

metros = float(input("Diga um valor em metros para conversao "))

centimetros = metros*100
milimetros = metros*1000

print(f"O valor em metros é {metros:.0f}MT , convertendo para centimetros fica {centimetros:.0f}CM e para milimetros fica  {milimetros:.0f}MM")
