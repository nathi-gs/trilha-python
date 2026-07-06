""" 
Lista 1 - Exercício 1

O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor
e dos impostos (aplicados ao custo de fábrica). Supondo que a porcentagem do distribuidor seja de 12%
do preço de fábrica e os impostos de 30% do preço de fábrica, fazer um programa em Python para ler o
custo de fábrica de um carro e imprimir o custo ao consumidor.

"""

custo_fabrica = float(input("Digite o valor do custo de fábrica: "))

distribuidor = custo_fabrica * 0.12
impostos = custo_fabrica * 0.30

custo_consumidor = custo_fabrica + distribuidor + impostos

print(f"Valor de Fábrica: R$ {custo_fabrica}\n")
print(f"Valor do distribuidor: {distribuidor}\n")
print(f"Valor do imposto: {impostos}\n")
print(f"Custo Total: R$ {custo_consumidor}\n")






