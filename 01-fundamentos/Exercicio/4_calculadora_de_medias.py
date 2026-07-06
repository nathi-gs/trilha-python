"""
Lista 1 - Exercicio 4

Elabore um programa em Python que leia as duas notas de
prova (P1 e P2) e duas notas de trabalho (T1 e T2) e
posteriormente exiba a mensagem ‘Aprovado’ ou ‘Não
aprovado’ dependendo dos valores obtidos, conforme as
regras de cálculo definidas a seguir:
    • Média de provas: MP = (P1 + P2)/2
    • Média de trabalhos: MT = (T1 + T2)/2
    • Média final: MF = 0,8MP + 0,2MT
    • Situação:
        ◦ Se MF ≥ 6,0 → aprovado
        ◦ Se MF < 6,0 → não aprovado
"""

#Lê as notas de prova e trabalhos
nota1 = float(input("Digite a nota da P1: "))
trabalho1 = float(input("Digite a nota da T1: "))
nota2 = float(input("Digite a nota da P2: "))
trabalho2 = float(input("Digite a nota da T2: "))

#calcula as medias
media_prova = (nota1 + nota2) / 2
media_trabalhos = (trabalho1 + trabalho2) / 2
media_final = (0.8 * media_prova) + (0.2 * media_trabalhos)

#Define se foi aprovado ou reprovado
if (media_final >= 6.0): 
    print("Aprovado")

if (media_final < 6.0):
        print("Não aprovado")




