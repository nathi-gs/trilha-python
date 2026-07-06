"""
Lista 1 - Exercicio 6

Crie um programa em Python que recebe um valor em reais e
o converte para outra moeda. Use um menu para escolher a
moeda de destino:
1. Dólar
2. Euro
3. Libra
4. Iene
O programa deve perguntar o valor em reais e exibir o valor
convertido para a moeda escolhida. Use valores fictícios para
as taxas de conversão:
1 Real = 0.19 Dólar
1 Real = 0.17 Euro
1 Real = 0.15 Libra
1 Real = 25 Ienes
"""

while True:
    valor = (float(input("\nDigite o valor que deseja converter: ")))

    print("\n************* MENU *************\n")
    print("1 Dólar")
    print("2 Euro")
    print("3 Libra")
    print("4 Iene")
    print("5 Sair")
    moeda = int(input("\nEscolha a moeda para conversão (1-5): "))
    
    if moeda == 1:
        print("\nValor convertido para Dólar: {:.2f}", valor * 0.19)
    
    elif moeda == 2:
        print("\nValor convertido para Euro: {:.2f}", valor * 0.17)
    
    elif moeda == 3: 
        print("\nValor convertido para Libra: {:.2f}", valor * 0.15)
    
    elif moeda == 4:
        print("\nValor convertido para Iene: {:.2f}", valor * 25)
    
    elif moeda == 5:
        print("\nConversões encerradas.")
        break
    
    else:
        print("\nOpção inválida. Digite um número de 1 a 5.") 
