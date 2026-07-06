"""
Uma escola aplicou provas em várias turmas e deseja 
registrar as maiores notas obtidas por seus alunos. Cada 
nota é representada por uma tupla no formato: 
(nome_do_aluno, nota, disciplina). Escreva um programa 
com o seguinte menu interativo:

1. Adicionar nota: o usuário deve informar o nome do aluno, 
a nota (float) e a disciplina, e esses dados devem ser 
adicionados como uma nova tupla à lista.

2. Mostrar melhor aluno por disciplina: para cada disciplina 
presente na lista, exiba o nome do aluno com a maior nota.

3. Consultar notas por aluno: o usuário digita o nome de um 
aluno e o programa mostra todas as notas dele, com a 
respectiva disciplina.

4. Exibir notas ordenadas (decrescente): mostre todas as 
tuplas da lista ordenadas da maior para a menor nota, no 
formato (nota, nome_do_aluno, disciplina).

5. Sair
O programa deve funcionar em laço até que o usuário 
escolha a opção de sair. Use tuplas para armazenar as notas 
e manipule-as sem alterar sua estrutura original. Utilizar 
função.

"""
def adicionar_nota(notas):
    nome = input("\nNome do aluno: ")
    nota = input("\nNota do aluno: ")

    while not (1 <= float(nota) <= 10):
        print("\nNota inválida!")
        nota = input("\nNota do aluno: ")

    disciplina = input("\nDigite a diciplina: ")

nota.append((nome, float(nota), disciplina))
print("\nNota Adicionada com sucesso!")

def melhor_por_disciplina(notas):
    if len(notas) == 0:
        print("\nNenhuma nota cadastrada.\n")
        return
    
    disciplinas = []

    for n in notas:
        if n[2] not in disciplinas:
             disciplinas.append(n[2])

    print("\nMelhor aluno por disciplina: ")

    for d in disciplinas:
        melhor_aluno = ""
        melhor_nota = -1
        for n in notas:
            if n[2] == d and n[1] > melhor_nota:
                melhor_nota = n[1]
                melhor_aluno = n[0]
            
        print(f"\n{d}: {melhor_aluno}, ({melhor_nota})")
    print("")

def consultar_por_aluno(notas):
    nome_busca = input("\nDigite o nome do aluno: ")

    encontrou = False

    for n in notas:
        if n[0].lower().strip == nome_busca.lower().strip:
            print(f"\n{n[2] : {n[1]}}\n")
            encontrou = True
    
    if not encontrou:
        print("\nNenhuma nota encontrada para este aluno.\n")

def obter_nota(tupla):
    return tupla[1]

def notas_ordenadas(notas):
    if len(notas) == 0:
        print("\nNenhuma nota cadastrada.\n")
        return
    
    ordenadas = sorted(notas, key=obter_nota, reverse=True)

    print("\nNotas Ordenadas (decrescente): ")
    for n in ordenadas:
        print(f"{n[1]:.2f}, {n[0]}, {n[2]} ")

def main():
    notas = []

    while True:
        print("\nMENU:")
        print("\n1 - Adicionar nota.")
        print("2 - Mostrar melhor aluno por disciplina.")
        print("3 - Consultar notas por aluno.")
        print("4 - Exibir notas ordenadas.")
        print("5 - Sair\n")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            adicionar_nota(notas)
        
        elif escolha == "2":
            melhor_por_disciplina(notas)
        
        elif escolha == "3":
            consultar_por_aluno(notas)
        
        elif escolha == "4":
            notas_ordenadas(notas)
        
        elif escolha == "5":
            print("\nSaindo do programa. Até mais!\n")
            break
        
        else: 
            print("\nOpção Inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()