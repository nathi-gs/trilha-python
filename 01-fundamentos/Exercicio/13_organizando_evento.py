"""
Uma universidade está organizando os dados de participação dos alunos em dois eventos acadêmicos: uma 
palestra sobre Inteligência Artificial e um workshop de Programação em Python. Os dados de presença são 
armazenados em dois conjuntos distintos: palestra_ia e workshop_python, contendo os nomes dos alunos que 
participaram de cada evento. Escreva um programa em Python com o seguinte menu interativo:

1. Adicionar aluno a um evento: O programa deve perguntar 
o nome do aluno e em qual evento ele participou (IA ou 
Python) e adicionar o nome ao conjunto correspondente.

2. Mostrar alunos que participaram de ambos os eventos: 
Exiba os nomes que aparecem nos dois conjuntos 
(interseção).

3. Mostrar alunos que participaram somente da palestra de 
IA: Exiba os nomes que estão no conjunto da palestra, mas 
não no workshop (diferença).

4. Mostrar alunos que participaram de pelo menos um evento:
Exiba a união dos dois conjuntos, sem repetições.

5. Verificar participação de um aluno: Solicite o nome de um 
aluno e diga se ele participou de ambos, somente um ou 
nenhum dos eventos.

6. Sair

O programa deve funcionar em laço até que o usuário 
escolha a opção de sair. Utilize operações com conjuntos 
(union, intersection, difference) para resolver as tarefas. 
Utilizar função.
"""

def adicionar_aluno(palestra_ia, workshop_python):
    nome_aluno = input("\nNome do aluno: ")
    palestra = input("Opções de palestras:\n\n 1 - Palestra IA \n\n 2 - Workshop Python \n\n Qual palestra ele participou: ")

    while not (palestra.isdigit() and 1 <= int(palestra) <= 2):
        print("\nPor favor, digite 1 ou 2.\n")
        palestra = input(" 1 - Palestra IA \n 2 - Workshop Python\n Qual palestra ele participou: ")
    
    if palestra == "1":
        palestra_ia.add(nome_aluno)
        print(f"\n{nome_aluno} adicionado com sucesso na Palestra IA.\n")
    
    elif palestra == "2":
        workshop_python.add(nome_aluno)
        print(f"\n{nome_aluno} adiconado com sucesso no Workshop Python.\n")


def listar_alunos_ambos_eventos(palestra_ia, workshop_python):
    print("\nAlunos que participaram de ambos os eventos: ", palestra_ia & workshop_python)

def listar_alunos_palestra_ia(palestra_ia, workshop_python):
    print("\nAlunos que participaram da palestra IA: \n", palestra_ia - workshop_python)

def listar_alunos_participaram(palestra_ia, workshop_python):
    print("\nAlunos que participaram de ambos os eventos: ", palestra_ia | workshop_python)

def verificar_participacao_aluno(palestra_ia, workshop_python):
    nome_aluno = input("\nDigite o nome do aluno: ")

    if nome_aluno in palestra_ia and nome_aluno in workshop_python:
        print(f"\n{nome_aluno} participou de ambos os eventos.\n")
    
    elif nome_aluno in palestra_ia:
        print(f"\n{nome_aluno} participou apenas da Palestra IA.\n")
    
    elif nome_aluno in workshop_python:
        print(f"\n{nome_aluno} participou apenas do Workshop Python.\n")
    
    else:
        print(f"{nome_aluno} não participou de nenhum evento.")


def main():
    palestra_ia = set()
    workshop_python = set()

    while True:
        print("\nMENU:\n")
        print("\n1 - Adicionar aluno a um evento.")
        print("\n2 - Mostrar alunos que participaram de ambos os eventos.")
        print("\n3 - Mostrar alunos que participaram somenta da palestra IA.")
        print("\n4 - Mostrar alunos que participaram de pelo menos um evento.")
        print("\n5 - Verificar participação de um aluno.")
        print("\n6 - Sair")

        escolha = input("\nEscolha uma opção de 1 a 5: ")

        if escolha == "1":
            adicionar_aluno(palestra_ia, workshop_python)
        
        elif escolha == "2":
            listar_alunos_ambos_eventos(palestra_ia, workshop_python)
        
        elif escolha == "3":
            listar_alunos_palestra_ia(palestra_ia, workshop_python)
        
        elif escolha == "4":
            listar_alunos_participaram(palestra_ia, workshop_python)
        
        elif escolha == "5":
            verificar_participacao_aluno(palestra_ia, workshop_python)
        
        elif escolha == "6":
            print("\nSaindo do programa. Até mais!")
            break
        
        else:
            print("\nOpção Inválida! Tente novamente.\n")



if __name__ == "__main__":
    main()