"""
Lista 2 - Exercicio 5

Faça um programa em Python que leia a temperatura em
graus Celsius e determine a classificação da temperatura:
    • Menor que 0°C: Frio extremo
    • De 0°C a 10°C: Frio
    • De 11°C a 25°C: Ameno
    • De 26°C a 35°C: Quente
    • Maior que 35°C: Muito quente
"""

#lê a temperatura
temp = int(input("Digite a temperatura (ºC): "))

if temp < 0:
    print("Frio extremo!!!!!!!")

elif (temp == 0 and temp <= 10):
    print("Frio")

elif (temp >= 11 and temp <= 25):
    print("Ameno")

elif (temp >= 26 and temp <= 35):
    print("Quente")

elif temp > 35:
    print("Muito quente")