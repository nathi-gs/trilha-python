"""
Lista 1 - Exercicio 7

Faça um programa em Python que simula as operações de
um banco. O programa deve apresentar um menu com as
seguintes opções:

1. Depositar (O programa deve pedir o valor a ser depositado
e somá-lo ao saldo)

2. Sacar (O programa deve pedir o valor a ser sacado e
subtrair do saldo, desde que o valor seja menor ou igual ao
saldo disponível)

3. Consultar Saldo (O programa deve exibir o saldo atual)
4. Sair (O programa termina)

O programa deve manter um saldo inicial de R$ 1000,00 e
permitir ao usuário realizar depósitos e saques até que ele
escolha a opção "Sair".
"""

saldo = 1000.00

print("************CAIXA ELETRÔNICO************")
print("SEJA BEM-VINDO\n")

while True:
    print("[MENU]")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("4 - Sair")

    opcao = int(input("\nEscolha uma opção. Digite um número (1-5): "))

    if opcao == 1:
        valor = float(input("\nDigite o valor para deposito: R$ "))
        
        if valor >= 0:
            saldo += valor
            print("Valor depositado com sucesso!\n")
        else:
            print("\nValor inválido. Digite um valor positivo.")
    
    elif opcao == 2:
        valor = float(input("\nDigite um valor para sacar: R$ "))

        if valor <= saldo:
            saldo -= valor
            print("\nValor sacado com sucesso.\n")
        else:
            print(f"\nValor do saldo insuficiente. Valor disponivel: R${saldo}")
    
    elif opcao == 3:
        print(f"\nSaldo Atual: R$ {saldo}")

    elif opcao == 4:
        print("\nObrigada por usar nossos serviços. Até Logo!")
        break
    
    else:
        print("Digite um número entre 1 e 5.")
