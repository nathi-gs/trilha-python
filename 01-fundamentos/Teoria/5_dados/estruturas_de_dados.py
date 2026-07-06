"""
Estruturas de dados são componentes fundamentais para armazenar e manipular coleções de dados.
Principais estruturas em Python: 
 -> Listas (List);
 -> Tuplas (Tuple);
 -> Conjuntos (Set);
 -> Dicionários (Dict).

 (LISTAS - LIST) -> São ordenadas, mutáveis e permitem valores duplicados.
                    Para criar uma lista declara-se uma variável com valores entre [].
                    Cada elemento dentro da lista é separado por ",".
                    Acessamos os elementos de uma lista pelo índice. 
                    O índice das listas começa em o.
                    Python permite índices negativos.
                    Pode imprimir a variável lista ou cada um de seus elementos.
                    Exemplo 1:

                    frutas = ["Banana", "Laranja", "Maçã", "Manga"]
                    print(frutas) #Imprime toda a lista
                    ["Banana", "Laranja", "Maçã", "Manga"]

                    frutas = ["Banana", "Laranja", "Maçã", "Manga"]
                    print(frutas[1]) #Imprime somente o item solicitado.
                    Laranja

                    Principais operações: 
                    *** append(): Adiciona um elemento no final da lista.
                    *** remove(): Remove a primeira ocorrência de um valor da lista.
                    *** pop(): Remove e retorna um elemento pelo índice (padrão: último)
                    *** insert(): Insere um elemento em uma posição específica.
                    *** sort(): Ordena a lista em ordem crescente ou alfabética. (Altera a lista original).
                    *** reverse(): Inverte a ordem dos elementos sem ordenar;
                    *** len(): Retorna o tamanho da lista (quantidade de elementos).

                    Exemplo 2:

                    #Adicionando elemento na lista | append()
                    frutas = ["Maça","Banana"]
                    frutas.append("Laranja")
                    print(frutas)
                    ["Maça","Banana","Laranja"] #Resposta no terminal

                    #Remover um elemento da lista | remove()
                    frutas = ["Maça", "Banana", "Laranja"]
                    frutas.remove("Banana")
                    print(frutas)
                    ["Maça","Laranja"] Resposta no terminal

                    #Remover e retornar o elemento removido no terminal pelo índice | pop()
                    frutas = ["Maça", "Banana", "Laranja"]
                    ultima = frutas.pop()
                    print(ultima)
                    Laranja #Resposta no terminal
                    print(frutas)
                    ["Maça", "Banana"] #Resposta no terminal

                    frutas.pop(0) 
                    Remove "Maça" (índice 0) #Resposta no terminal

                    #Inseri um elemento pelo índice | insert()
                    frutas = ["Banana", "Laranja"]
                    frutas.insert(0, "maça") #índice 0
                    print(frutas)
                    ["Maça", "Banana", "Laranja"] #Resposta no terminal

                    #Ordena a lista em ordem crescente | sort()
                    numeros = [3, 1, 4, 2]
                    numeros.sort()
                    print(numeros)
                    [1, 2, 3, 4] #Resposta no terminal

                    #Inverte a ordem dos elementos sem ordenar | reverse()
                    letras = ["a", "b", "c"]
                    letras.reverse()
                    print(letras)
                    ["c", "b", "a"] #Resposta no terminal

                    #Retornar o tamanho da lista | len()
                    frutas = ["Maça", "Banana", "Laranja"]
                    print(len(frutas))
                    3 #Resposta no terminal

"""

print("Exemplo 1: \n")

frutas = ["Banana", "Laranja", "Maçã", "Manga"]
print("Imprimindo Toda a Lista:")
print(frutas) #Imprime toda a lista
                    
frutas = ["Banana", "Laranja", "Maçã", "Manga"]
print("\nImprimindo somente um elemento da lista, pelo índice.")
print(frutas[1]) #Imprime somente o item solicitado.

print("\n------------------------------------------\n")

print("Exemplo 2: \n")

print("Adicionando elemento na lista | append()")
frutas = ["Maça","Banana"]
frutas.append("Laranja")
print(frutas)

print("\nRemover um elemento da lista | remove()")
frutas = ["Maça", "Banana", "Laranja"]
frutas.remove("Banana")
print(frutas)

print("\nRemover e retornar o elemento removido no terminal pelo índice | pop()")
frutas = ["Maça", "Banana", "Laranja"]
ultima = frutas.pop()
print(ultima)
print(frutas)
frutas.pop(0) 

print("\nInseri um elemento pelo índice | insert()")
frutas = ["Banana", "Laranja"]
frutas.insert(0, "maça") #índice 0
print(frutas)

print("\nOrdena a lista em ordem crescente | sort()")
numeros = [3, 1, 4, 2]
numeros.sort()
print(numeros)

print("\nInverte a ordem dos elementos sem ordenar | reverse()")
letras = ["a", "b", "c"]
letras.reverse()
print(letras)

print("\nRetornar o tamanho da lista | len()")
frutas = ["Maça", "Banana", "Laranja"]
print(len(frutas))


"""
(TUPLAS) -> Parecidas com lista
            São imutáveis. Uma vez criada, não pode modificar os elementos da tupla.
            Usadas para armazenar coleções de dados que devem permanecer imutáveis.
            Podem ser usadas como chaves de dicionários ou elementos em conjunto.
            Sintaxe: Usamos parenteses para criar uma tupla ou apenas virgulas.
                     minha_tupla = (1, 2, 3) ou minha_tipla = 4, 5, 6
                     
                     Uma tuplia com um único elemento precisa de virgula.
                     tupla_unitaria = (10,)
            Exemplo 3:

            #Visualizar um elemento pelo índice:
            cores = ("vermelho", "verde", "azul")
            print(cores[0])
            vermelho #Resposta do terminal

            #Desempacotar tupla:
            ponto = (3, 4)
            x, y = ponto
            print(x)
            3 #Resposta do terminal
            print(y)
            4 #Resposta do terminal

            #Lista de tuplas:
            alunos = [("Maria",8.5), ("Bruno",7.0), ("Carla", 9.3)]

            for nome, nota in alunos:
                print(f"{nome} tirou nota{nota}")

            #Usar tuplas como cahves em dicionários:
            coordenadas = {(0, 0): "origem", (1,2): "ponto A"}
            print(coordenadas[(1, 2)])
            ponto A #Resposta do terminal

"""
print("\n------------------------------------------\n")

print("Exemplo 3: ")

print("\nVisualizar um elemento pelo índice: ")
cores = ("vermelho", "verde", "azul")
print(cores[0])

print("\nDesempacotar tupla: ")
ponto = (3, 4)
x, y = ponto
print(x)
print(y)

print("\nLista de tuplas: ")
alunos = [("Maria",8.5), ("Bruno",7.0), ("Carla", 9.3)]

for nome, nota in alunos:
    print(f"{nome} tirou nota{nota}")

print("\nUsar tuplas como cahves em dicionários: ")
coordenadas = {(0, 0): "origem", (1,2): "ponto A"}
print(coordenadas[(1, 2)])



"""
(CONJUNTOS) -> São coleções não ordenadas de elementos únicos (sem repetição)
               Úteis para garantir que não haja duplicatas e para operações matemáticas como união.
               Sintaxe: meu_conjunto = {1, 2, 3, 4, 5}
                        print(meu_conjunto)

               Características importantes: 
                ** Elementos não podem se repetir.
                ** Conjuntos são mutáveis, pode adicionar ou remover elementos.
                ** Os elementos precisam ser imutáveis (ex.: números, strings, tuplas).
                ** Listas não podem ser elementos de conjuntos.

                Exemplo 4: 
                
                #Elementos não podem se repetir:
                conjunto = {1, 2, 2, 3}
                print(conjunto)
                {1, 2, 3} #Resposta do terminal

                #Adicionar elementos:
                conjunto = {1, 2, 3}
                conjunto.add(4) #Adiciona 4
                print(conjunto)
                {1, 2, 3, 4} #Resposta do terminal

                #Remover elementos:
                conjunto = {1, 2, 3, 4}
                conjunto.discard(2) #Remove 2
                print(conjunto)
                {1, 3, 4}

                #Operações comuns com conjuntos:
                A = {1, 2, 3, 4}
                B = {3, 4, 5, 6}

                print("União:", A|B)
                {1, 2, 3, 4, 5, 6} #Resposta do terminal

                print("Interseção:", A & B)
                {3, 4} #Resposta do terminal

                print("Diferença A - B:", A - B)
                {1, 2} ##Resposta do terminal

                print("Diferença B - A:", B - A)
                {5, 6} #Resposta do terminal

"""

print("\n------------------------------------------\n")
print("Exemplo 4: ")
print("\nElementos não podem se repetir")
conjunto = {1, 2, 2, 3}
print(conjunto)

print("\nAdicionar elementos")
conjunto = {1, 2, 3}
conjunto.add(4) #Adiciona 4
print(conjunto)

print("\nRemover elementos:")
conjunto = {1, 2, 3, 4}
conjunto.discard(2) #Remove 2
print(conjunto)

print("\nOperações comuns com conjuntos:")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("União:", A|B)
print("Interseção:", A & B)
print("Diferença A - B:", A - B)
print("Diferença B - A:", B - A)

"""
(DICIONARIOS) -> Armazenam pares de chave-valor.
                 Cada chave é única e mapeia para um valor.
                 Ótimos para representar dados que associam uma informação a outra.
                 Exemplo 5:
                 
                 #Criando um dicionário
                 pessoa = {
                    "nome": "Maria",
                    "idade": 25,
                    "cidade": "São Paulo"
                    }

                 print(pessoa)

                 #Acessando valores
                 print(pessoa["nome"]) 
                 Maria #Resposta do terminal
                 print(pessoa.get("idade"))
                 25 #Resposta do terminal

                 #Adiconar ou modificar elementos:
                 pessoa["email"] = "maria@example.com"
                 pessoa["idade"] = 26

                 #Remover elementos:
                 del pessoa["cidade"]  #Remove a chave cidade
                 email = pessoa.pop("email") #Remove e retorna o valor associado a 'email'

                 #Iterar sobre dicionários
                 for chave, valor in pessoa.items():
                    print(f"{chave}:{valor}")
"""
print("\n------------------------------------------\n")

print("\nExemplo 5: ")
print("Criando um dicionário: ")
pessoa = {
"nome": "Maria",
"idade": 25,
"cidade": "São Paulo"
}

print(pessoa)

print("\nAcessando valores: ")
print(pessoa["nome"]) 
print(pessoa.get("idade"))

print("\nAdiconar ou modificar elementos: ")
pessoa["email"] = "maria@example.com"
pessoa["idade"] = 26

print("\nRemover elementos:")
del pessoa["cidade"]  #Remove a chave cidade
print(pessoa)
email = pessoa.pop("email") #Remove e retorna o valor associado a 'email'
print(pessoa)

print("\nIterar sobre dicionários")
for chave, valor in pessoa.items():
    print(f"{chave}:{valor}")
