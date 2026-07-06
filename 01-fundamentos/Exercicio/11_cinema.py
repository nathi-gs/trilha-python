"""
Escreva um programa em Python que simule o controle de 
uma sala de cinema. O cinema possui 10 assentos 
numerados de 1 a 10, e o programa deve manter uma lista de
ocupação dos assentos (com valores booleanos, onde True 
indica ocupado e False indica livre). O usuário poderá 
interagir com o sistema por meio de um menu com as 
seguintes opções:

1. Reservar um assento
2. Liberar um assento
3. Mostrar mapa de ocupação (exibindo quais assentos 
estão ocupados e quais estão livres)
4. Sair

O programa deve impedir a reserva de assentos já ocupados 
e a liberação de assentos que já estão livres. Utilizar função.

"""
def reservar_assento(assentos):
    numero = input("\nEscolha o assento para reservar de 1 á 10 : ")

    while not (numero.isdigit() and 1 <= int(numero) <= 10):
        print("\nNúmero de assento inválido!")
        numero = input("\nDigite um número válido entre 1 e 10: ")
    
    if assentos[int(numero) - 1] == False:
        assentos[int(numero) -1] = True
        print(f"\nAssento {numero} reservado com sucesso.")
    else:
        print(f"\nAssento {numero} já esta ocupado.\n")


def liberar_assento(assentos):
     numero = input("\nEscolha o assento para liberar de 1 á 10 : ")

    while not (numero.isdigit() and 1 <= int(numero) <= 10):
        print("\nNúmero de assento inválido!")
        numero = input("\nDigite um número válido entre 1 e 10: ")
    
    if assentos[int(numero) - 1] == True:
        assentos[int(numero) -1] = False
        print(f"\nAssento {numero} liberado com sucesso.")
    else:
        print(f"\nAssento {nmero} já está livre.\n")

def mostrar_mapa(assentos):
    print("\nMapa de Ocupação dos Assentos")
    
    for i in range(10):
        if assentos[i] == True:
            status = "Ocupado"
        else:
            status = "Livre"
        print(f"Assento {i+1}: {status}")
    print()


def main():
    assentos = [False] * 10

    while True:
        print("\n*****************************")
        print("********* CINEPOLIS *********")
        print("*****************************")
        print("1 - Reservar um assento.")
        print("2 - Liberar um assento.")
        print("3 - Mostrar mapa de ocupação.")
        print("4 - Sair.")

    escolha = input("Digite um número de 1 à 4: ")

    if escolha == "1":
        reservar_assento(assentos)
    
    elif escolha == "2":
        liberar_assento(assentos)
    
    elif escolha == "3":
        mostrar_mapa(assentos)
    
    elif escolha == "4":
        print("\nSaindo do Programa.")
        break
             
    else:
        print("\nOpção inválida! Digite um número de 1 à 4.")



if __name__ == "__main__":
    main()