from livro import Livro

def cadastrar_livro(acervo):
    titulo = input("\nDigite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    id_livro = input("Digite o ID do livro: ")

    novo_livro = Livro(titulo, autor, id_livro)

    acervo.append(novo_livro)

    print("\nLivro cadastrado com sucesso!\n")