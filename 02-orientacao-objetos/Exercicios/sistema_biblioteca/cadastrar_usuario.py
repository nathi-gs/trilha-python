from usuario import Usuario

def cadastrar_usuario(usuario_cadastrado):
    nome = input("\nDigite o nome do usuario: ")
    matricula = input("Digite a matricula do usuario: ")

    novo_usuario = Usuario(nome, matricula)

    usuario_cadastrado.append(novo_usuario)

    print("\nUsuario cadastrado com sucesso!\n")
