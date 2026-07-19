class Usuario:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__livros_emprestados = []
    
    def get_nome(self):
        return self.__nome
    
    def get_matricula(self):
        return self.__matricula
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    
    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula