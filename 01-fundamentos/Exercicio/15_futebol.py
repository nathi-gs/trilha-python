"""
Você foi contratado para desenvolver um sistema simples 
para gerenciar um campeonato de futebol. O sistema deve 
usar um dicionário onde as chaves são os nomes dos times e
os valores são os pontos conquistados. O programa deve 
apresentar o seguinte menu:

1. Adicionar time: permite cadastrar um novo time com 0 
pontos iniciais.

2. Registrar resultado de partida: o usuário informa os nomes 
de dois times e o resultado da partida (quantidade de gols de 
cada time). O programa atualiza os pontos dos times: 3 
pontos para o vencedor, 1 ponto para empate, 0 para o 
perdedor.

3. Mostrar classificação: exibe a lista dos times e seus 
pontos, ordenada do maior para o menor número de pontos.

4. Remover time: permite remover um time da competição.

5. Sair

O programa deve funcionar em loop até o usuário escolher 
sair. Utilizar função
"""
def adiconar_time(campeonato):
    time = input("\nAdicione o nome do time: ").strip().lower()

    if time in campeonato:
        print("\nTime já cadastrado.")
    else:
        campeonato[time] = 0
        print(f"\nTime '{time}' adicionado com 0 pontos.\n")

def registrar_resultado(campeonato):
    time1 = input("Nome do primeiro time: ").strip().lower()
    time2 = input("Nome do primeiro time: ").strip().lower()

    if time1 not in campeonato or time2 not in campeonato:
        print("\nAmbos os times devem estar cadastrados.")
        return
    
    gols1 = int(input(f"\nGols do {time1}: "))
    gols2 = int(input(f"\nGols do {time2}: "))

    if gols1 > gols2:
        campeonato[time1] += 3
        print(f"{time1} venceu e ganhou 3 pontos.")
    elif gols1 < gols2:
        campeonato[time] += 3
        print(f"{time2} venceu e ganhou 3 pontos.")
    else:
    campeonato[time1] += 1
    print(f"{time1} venceu e ganhou 1 ponto.")


    campeonato[time2] += 1
        print(f"{time2} venceu e ganhou 1 ponto.")


def obter_pontos(item):
    return item[1]

def mostrar_classificacao(campeonato):
    if not campeonato:
        print("\nNenhum time cadastrado.\n")
        return
    
    classificacao = sorted(campeonato, key=obter_pontos, reverse=True)

    print("\nClassificação: ")
    for time, pontos in enumerate(campeonato):
        print(f"{posicao + 1} - {time}: {campeonato[time]} ponto(s)")
    print()

def remover_time(campeonato):
    time = input("Nome do time a remover: ").strip().lower

    if time in campeonato:
        del campeonato[time]
        print(f"\nTime {time} removido do campeonato!")
    else:
        print("\nTime não encontrado.\n")




def main():
    campeonato = {}

    while True:
        print("\nMENU:")
        print("\n1 - Adicionar time.")
        print("2 - Registrar resultado de partida.")
        print("3 - Mostrar classificação.")
        print("4 - Remover time.")
        print("5 - Sair\n")

        escolha = input("\nEscolha uma opção (1-5): ")

        if escolha == "1":
            adiconar_time(campeonato)
        
        elif escolha == "2":
            registrar_resultado(campeonato)
        
        elif escolha == "3":
            mostrar_classificacao(campeonato)
        
        elif escolha == "4":
            remover_time(campeonato)
        
        elif escolha == "5":
            print("\nSaindo do programa. Até mais!\n")
            break
        
        else: 
            print("\nOpção Inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()