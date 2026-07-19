from string import AnalisadorString

def main():
    palavra = input("Digite uma palavra: ")

    analisador = AnalisadorString(palavra)

    print(f"\nNúmero de caracteres: {analisador.numero_de_caracteres()}")
    print(f"\nEm maiúsculas: {analisador.em_maiusculo()}")
    print(f"\nEm minúsculo: {analisador.em_minusculo()}")
    print(f"\nNúmero de vogais: {analisador.contar_vogais()}")

    if analisador.contem_ifb():
        print("\nA substring 'IFB' aparece na palavra.\n")
    else:
        print("\nA substring 'IFB' não aparece na palavra.\n")




if __name__ == "__main__":
    main()