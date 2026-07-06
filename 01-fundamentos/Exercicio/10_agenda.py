"""
Você foi contratado para desenvolver um pequeno sistema de
gerenciamento de uma lista de tarefas pessoais. Escreva um 
programa em Python que utilize um menu interativo para 
permitir ao usuário as seguintes opções:

1. Adicionar uma nova tarefa
2. Listar todas as tarefas
3. Remover uma tarefa pelo nome
4. Sair do programa

O programa deve manter as tarefas em uma lista e permitir 
que o usuário realize várias operações até optar por sair. 
Utilizar função
"""

def adicionar_tarefa(tarefas):
    descricao = input("\nDescrição da tarefa: \n")

    tarefa = {
        "descrição": descricao
    }

    tarefas.append(tarefa)
    print("\nTarefa adicionada com sucesso!\n")

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("\nNenhuma tarefa encontrada.\n")
        return
    
    tarefas.sort

    print("\nTAREFAS: ")
    for i, t in enumerate(tarefas):
        print(f"{i + 1}. {t["descrição"]}")

def remover_tarefa(tarefas):
    if len(tarefas) == 0:
        print("\nNenhuma tarefa para remover.\n")
    
    listar_tarefas(tarefas)
    escolha = input("\nDigite o número da tarefa pare ser removida: \n")

    while not (escolha.isdigit() and 1 <= int(escolha) <= len(tarefas)):
        print("\nNúmero inválido, tente novamente!\n")
        escolha = input("\nDigite o número valido.\n")
    
    indice = int(escolha) - 1
    del tarefas[indice]
    print("\n Tarefa removida com sucesso!\n")

def main():
    tarefas = []

    while True:
        print("**** MENU ****")
        print("1 - Adicionar uma nova tarefa\n")
        print("2 - Listar todas as tarefas\n")
        print("3 - Remover uma tarefa pelo nome\n")
        print("4 - Sair do programa\n")
    
        opcao = input("Escolha uma opção de 1 a 5: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        
        elif opcao == "2":
            listar_tarefas(tarefas)
        
        elif opcao == "3":
            remover_tarefa(tarefas)
        
        elif opcao == "4":
            print("Saindo do programa.")
            break 
            
        else:
            print("Opção inválida! Digite um número de 1 a 5.\n")


if __name__ == "__main__":
    main()
