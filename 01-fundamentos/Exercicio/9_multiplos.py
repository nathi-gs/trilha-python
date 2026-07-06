"""
Faça um programa em Python que imprima todos múltiplos de
x, entre 1 e 100, onde x é um número informado pelo usuário.
Utilizar função.
"""

def imprimir_multiplos(x):
    print(f"\nMúltiplos de {x} entre 1 e 100: ")

    for num in range(1,101):
        if num % x == 0:
            print(num, end = " ")
    
    print()
    print()


def main():
    x = input("\nDigite um número inteiro: ")

    while not (x.isdigit() and 1 <= int(x) <= 100):
        print("\nPor fovor, digite um númeor inteiro entre 1 e 100!")
        x = input("\nDigite um número inteiro: ")

    imprimir_multiplos(int(x))



if __name__ == "__main__":
    main()