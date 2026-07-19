from progressao import Progressao

def main():

    print("\n********** Progressão Aritmética **********\n")
    n = int(input("\nDigite o número de termos da progressao aritmética (n): "))
    a1 = float(input("\nDigite o primeiro termo da progressão (a1): "))
    r = float(input("Digite a razão (r): "))

    pa = Progressao(n, a1, r)

    termos = pa.gerar_termos()
    
    print("Termos da P.A:")
    contador = 1
    for termo in termos:
        print(f"\nTermo {contador}: {termo}")
        contador += 1
    
    soma = pa.calcular_soma()

    print(f"\nSoma dos {n} termos: {soma}")




if __name__ == "__main__":
    main()