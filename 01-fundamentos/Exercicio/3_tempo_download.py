""" 
Lista 1 - Exercicio 3

Faça um programa que peça o tamanho de um arquivo para
download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).
"""

#Lê o tamanho e a velocidade dos arquivos para download
tamanho_arquivo = float(input("Qual o tamanho de um arquivo para download em MB: "))
velocidade_link = float(input("Qual a valocidade de um link de internet em Mbps: "))

#converte a velocidade do link em MBps
valocidade_total = velocidade_link / 8

#calcula o tempo em segundos
tempo_segundos = tamanho_arquivo / valocidade_total

#calcula o tempo em minutos
tempo_minutos = tempo_segundos / 60

#imprime resultados
print(f"O tamanho do arquivo é: {tamanho_arquivo}")
print(f"A velocidade do arquivo é: {velocidade_link}")
print(f"O tempo aproximado para download: {tempo_minutos:.2f} minutos")
print(f"O tempo aproximado para download: {tempo_segundos:.2f} segundos")






