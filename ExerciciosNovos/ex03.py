'''
    Aluguel de carros:

    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

    Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
'''


km_percorrido = float(input("quantos kilometros foi percorrido? "))
dia_alugados = float(input("quantos dias o carro foi alugado? "))

total_dia = dia_alugados*60 
km_total = km_percorrido*0.15
total = total_dia+km_total

print(f"O carro foi alugado por {dia_alugados:.0f} dias , ficando no valor de R${total_dia:.2f}reais pelos dias alugados e rodou {km_percorrido:.0f} kilometros , totalizando o valor de R${km_total:.2f} reais ,dando um total km/dia pelo carro alugado de R${total:.2f} reais.")




