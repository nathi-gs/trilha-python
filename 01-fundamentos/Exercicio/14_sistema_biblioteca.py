"""
Uma livraria quer controlar seu estoque usando um dicionário onde as chaves são os títulos dos livros e os 
valores são a quantidade disponível em estoque.  Implemente um programa com as seguintes funcionalidades:

1. Adicionar um livro ao estoque: o usuário informa o título e a
quantidade (se o livro já existir, some a quantidade nova à 
existente).

2. Remover unidades de um livro: o usuário informa o título e 
a quantidade a remover; o programa deve atualizar o estoque
e avisar se o estoque ficar zerado ou se o livro não existir.

3. Consultar quantidade de um livro: o usuário digita o título e 
o programa mostra a quantidade disponível ou informa que o 
livro não está no estoque.

4. Mostrar todos os livros com suas quantidades ordenados 
alfabeticamente.

5. Sair

O programa deve repetir o menu até que o usuário escolha 
sair. Utilizar função

"""

def adicionar_livro(estoque):
    titulo = input("\nDigite o título do livro: ")
    quantidade = input("\nDigite a quantidade de títulos: ")

    while not (quantidade.isdigit()):
        print("\nPor favor, digite uma quantidade valida.")
        quantidade = input("\nDigite a quantidade de títulos: ")
        
    quantidade_int = int(quantidade)

    if titulo in estoque:
        estoque[titulo] = estoque[titulo] + quantidade_int
        print(f"\nQuantidade atualizada! Agora temos {estoque[titulo]} unidades de {titulo}.")
    
    else:
        estoque[titulo] = quantidade_int
        print(f"\n{titulo} foi adicionado no estoque.")

def remover_unidade(estoque):
    titulo = input("\nDigite o titulo a ser removido: ")
    quantidade = input("\nDigite a quantidade a ser removida: ")

    while not (quantidade.isdigit()):
        print("\nPor favor, digite uma quantidade valida.")
        quantidade = input("\nDigite a quantidade de títulos: ")
        
    quantidade_int = int(quantidade)

    if titulo not in estoque:
        print("Este livro não existe no estoque.")

    else: 
        estoque[titulo] = estoque[titulo] - quantidade_int
        print("Livro removido com sucesso!")
        
        
    if estoque[titulo] <= 0:
        print("Aviso: O estoque deste livro zerou!")

def consultar_quantidade(estoque):
    pass

def mostrar_todos_os_livros(estoque):
    pass



def main():
    estoque = {}

    while True:
        print("\nMENU: ")
        print("\n1 - Adiconar livro no estoque.")
        print("\n2 - Remover unidades de um livro.")
        print("\n3 - Consultar quantidade de um livro.")
        print("\n4 - Mostrar todos os livros.")
        print("\n5 - Sair.")

        escolha = input("\n Escolha uma opção: ")

        if escolha == "1":
            adicionar_livro(estoque)
        
        elif escolha == "2":
            remover_unidade(estoque)
        
        elif escolha == "3":
            consultar_quantidade(estoque)
        
        elif escolha == "4":
            mostrar_todos_os_livros(estoque)
            break
        
        else:
            print("\nOpção Inválida! Tente novamente.\n")



if __name__ == "__main__":
    main()