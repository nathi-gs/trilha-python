"""
Lista 1 - Exercicio 8

Faça um programa em Python que leia dois valores inteiros, x
e y. Por meio de multiplicações sucessivas, calcule e exiba a
função de exponenciação xy (Obs: quando o valor de y for 0,
não importa o valor de x, o resultado sempre será 1. Utilizar
função).
"""

def potencia(base, expoente):
    if expoente == 0:
        return 1
    resultado = 1

    for _ in range(expoente):
        resultado *= base
    return resultado
    
    

def main():
    x = input("\nDigite o valor x (base): ")
    while not(x.isdigit()):
        print("\nPor favor, entre com um número inteiro!")
        x = input("\nDigite o valor x (base): ")


    y = input("\nDigite o valor y (expoente): ")
    while not(y.isdigit()):
        print("\nPor favor, entre com um número inteiro!")
        y = input("\nDigite o valor y (expoente): ")

    resultado = potencia(int(x), int(y))

    print(f"{x}^{y} = {resultado}\n")




if __name__ == "__main__":
    main()