class Usuario:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__livros_emprestados = []
    
    def get_nome(self):
        return self.nome
    
    def get_matricula(self):
        return self.matricula
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def set_matricula(self, nova_matricula):
        self.matricula = nova_matricula