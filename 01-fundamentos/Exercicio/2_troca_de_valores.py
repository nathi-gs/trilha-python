"""
Lista 1 - Exercicio 2

Faça um programa em Python que leia dois números inteiros
quaisquer para as variáveis A e B, efetue a troca dos valores
de forma que A passe a armazenar o valor de B e que B
passe armazenar o valor de A e que imprima os valores
trocados.
"""

#lê os valores de A e B
a = int(input("Digite um número inteiro para A: "))
b = int(input("Digite um número inteiro para B: "))

#faz a troca dos valores
valor1 = a and b
valor2 = b and a

#imprime os valores originais e trocados
print(f"Valor original de A: {a}")
print(f"O valor de A passa a ser: {valor1}")
print(f"\nValor original de B: {b}")
print(f"O valor de B passa a ser: {valor2}")



