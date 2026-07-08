import livro
import usuario

def emprestar_livro(self, livro):
        self.__livros_emprestados.append(livro)
        print(f"\n{self.nome} pegou emprestado o livro '{livro.get_titulo()}'.\n")