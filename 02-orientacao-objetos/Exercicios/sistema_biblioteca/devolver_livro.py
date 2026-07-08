import livro
import usuario

def devolver_livro(self, id_livro):
        for livro in self.__livros_emprestados:
            if livro.get_id_livro() == id_livro:
                self.__livros_emprestados.remove(livro)
                print(f"\n{self.__nome} devolveu o livro '{livro.get_titulo()}'.\n")
                return
        
        print(f"\n{self.__nome} não possui um livro com ID '{id_livro}'\n")