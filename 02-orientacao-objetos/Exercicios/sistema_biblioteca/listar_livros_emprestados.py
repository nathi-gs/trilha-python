from livro import Livro
from usuario import Usuario

def listar_livros_emprestados(self):
        if not self.__livros_emprestados:
            print("\nNenhum livro emprestado.\n")
        else:
            print("\nLivros emprestados: \n")
            for livro in self.__livros_emprestados:
                print(f"- {livro.get_titulo()} ({livro.get_id_livro()})")
            print()