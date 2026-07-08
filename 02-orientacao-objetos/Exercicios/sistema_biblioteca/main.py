from livro import Livro
from usuario import Usuario
from emprestar_livro import emprestar_livro
from devolver_livro import devolver_livro
from listar_livros_emprestados import listar_livros_emprestados
from cadastrar_usuario import cadastrar_usuario
from cadastrar_livro import cadastrar_livro

#CASA: CRIAR MENU ok; CADASTRAR LIVRO ok; CADASTRAR USUARIO; EMPRESTAR LIVRO; DEVOLVER LIVRO; LISTAR LIVROS EMPRESTADOS

def main():
    acervo = []
    usuario_cadastrado = []

    
    while True:
        print("****** MENU BIBLIOTECA ******")
        print("1 - Cadastrar Usuario")
        print("2 - Cadastrar Livro")
        print("3 - Emprestar livro")
        print("4 - Listar livros emprestados")
        print("5 - Devolver livro")
        
        escolha = input("\n3Escolha uma opção de 1 a 3: ")
        
        if escolha == "1":
            cadastrar_usuario(usuario_cadastrado)
        
        elif escolha == "2":
            cadastrar_livro(acervo)
        
        elif escolha == "3":
            emprestar_livro()
            
        elif escolha == "4":
            listar_livros_emprestados()
            
        elif escolha == "5":
            devolver_livro()
            break
            
        else:
            print("Opção inválida! Digite um número de 1 a 3: ")


if __name__ == "__main__":
    main()