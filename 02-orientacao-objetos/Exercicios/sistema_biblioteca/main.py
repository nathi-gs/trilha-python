from livro import Livro
from usuario import Usuario
from emprestar_livro import emprestar_livro
from devolver_livro import devolver_livro
from listar_livros_emprestados import listar_livros_emprestados


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
        print("6 - Sair")
        
        escolha = input("\nEscolha uma opção de 1 a 6: ")
        
        if escolha == "1":
            nome = input("\nDigite o nome do usuario: ")
            matricula = input("Digite a matricula do usuario: ")
            
            novo_usuario = Usuario(nome, matricula)
            
            usuario_cadastrado.append(novo_usuario)
            
            print("\nUsuario cadastrado com sucesso!\n")
        
        elif escolha == "2":
            titulo = input("\nDigite o nome do livro: ")
            autor = input("Digite o nome do autor: ")
            id_livro = input("Digite o ID do livro: ")
                
            novo_livro = Livro(titulo, autor, id_livro)
                
            acervo.append(novo_livro)
                
            print("\nLivro cadastrado com sucesso!\n")
        
        elif escolha == "3":
            if len(usuario_cadastrado) == 0:
                print("\nCadastre um usuário antes de realizar empréstimos.\n")
                continue

            if len(acervo) == 0:
                print("\nNão há livros cadastrados.\n")
                continue
                
            matricula = input("\nMatrícula do usuário: ")
                
            usuario = None
                
            for u in usuario_cadastrado:
                if u.get_matricula() == matricula:
                    usuario = u
                        
            if usuario is None:
                print("\nUsuário não encontrado.\n")
                continue
                            
            id_livro = input("\nID do livro: ")
                            
            livro = None
                            
            for l in acervo:
                if l.get_id_livro() == id_livro:
                    livro = l

            if livro is None:
                print("\nLivro não encontrado.\n")
            else:
                usuario.emprestar_livro(acervo)
            
        elif escolha == "4":
            if len(usuario_cadastrado) == 0:
                print("\nCadastre um usuário antes de devolver livros.\n")
                continue
             
            matricula = input("\nMatrícula do usuário: ")

            usuario = None

            for u in usuario_cadastrado:
                if u.get_matricula() == matricula:
                    usuario = u

            if usuario is None:
                print("\nUsuário não encontrado.\n")
                continue
             
            id_livro = input("\nID do livro: ")
            usuario.devolver_livro(id_livro)

        elif escolha == "5":
            if len(usuarios) == 0:
                print("\nCadastre um usuário antes de listar empréstimos.\n")
                continue
             
            matricula = input("\nMatrícula do usuário: ")

            usuario = None

            for u in usuarios:
                if u.get_matricula() == matricula:
                    usuario = u

            if usuario is None:
                print("\nUsuário não encontrado.\n")
            else:
                usuario.listar_livros_emprestados()

        elif opcao == "6":
            print("\nEncerrando programa...\n")
            break

        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()