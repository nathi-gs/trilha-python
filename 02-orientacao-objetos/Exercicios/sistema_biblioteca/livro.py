class Livro:
    def __init__(self, titulo, autor, id_livro):
        self.__titulo = titulo
        self.__autor = autor
        self.__id_livro = id_livro
    
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_id_livro(self):
        return self.__id_livro
    
    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    def set_autor(self, novo_autor):
        self.__autor = novo_autor
    
    def set_id_livro(self, novo_id_livro):
        self.__id_livro = novo_id_livro