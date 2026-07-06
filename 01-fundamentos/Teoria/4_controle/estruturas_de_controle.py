"""
Estruturas de controle são os comandos que controlam o fluxo de execução de um programa.

Tipos: 

>> Sequenciais<<
  Segue uma linha linear de acontecimentos.

>> Condicionais <<
  Executar blocos diferentes de código com base em uma condição
  #Chaves: if, elif, else


  (if) -> Executa um bloco de código se a condição for verdadeira.
          Sintaxe Básica: " if condição: "
          Exemplo 1:

          if idade >= 18:
            print("Maior de idade")

    
    (if ... else) -> Executa um bloco se a condição for verdadeira e a outra falsa.
                     Sintaxe: "if condição: 
                                else: "
                    Exemplo 2:

                    if x > 0: 
                        print("Positivo")
                    else: 
                        print("Negativo")

    
    (if ... elif ... else) -> Testa múltiplas condições em sequência (como "se não, se...)
                              Sintaxe: "if condição:
                                        elif condição:
                                        else: "
                              Exemplo 3: 
                                if nota >= 90:
                                    print("A")
                                elif nota >= 60:
                                    print("B")
                                else:
                                    print("F")
    
    (if aninhado) -> Um if dentro de outro, para decisões mais detalhadas ou hierárquicas.
                     Sintaxe: "if condição:
                                 if outra: "
                    
                    Exemplo 4:

                    if numero > 0:
                        if numero % 2 == 0:
                            print("Par positivo")


>> Repetição <<
  Repetir um bloco de código várias vezes. Laços ou loops.
  #Chaves: for, while
  Conjunto de Princípios: 
   ** Um início: Elemento de controle que diz onde a repetição começa.
   ** Um fim: Um teste que deve dizer se a repetição continua ou não.
   ** Um incremento: Ação que nos leva do ponto de início até chegarmos ao ponto final.


   (WHILE) -> Estrutura baseada em uma condição lógica.
              Use while quando quiser repetir até que uma condição seja satisfeita, sem saber antecipadamente o número de vezes.
              Baseado em uma condição: "while condição: "
              Exemplo 4: 

              i = 0 -> (Inicialização: A variavével de controle i é inicializada antes e fora do bloco de comando while)
              while (i<3): -> (O fim: O fim da repetição é determinado por uma expressão booleana. Enquanto o resultado da expressão for true, a repetição continua.)
                print(i)
                i+=1 -> (Incremento: O incremento é explicitamente feito na variável de controle. Ele deve ser feito dentro do corpo do while.)
    

    (FOR) -> Estrutura que percorre uma sequência ou intervalo.
             Use for quando souber quantas vezes precisa repetir ou quiser percorrer elementos de uma coleção.
             Baseado em uma sequência: "range, lista, string, etc."
             Exemplo 5: 

             time = ["Taffarel", "Aldair", "Marcio", "Romario"] -> LISTA

             for jogador in time:
                print (jogador)
            
            Explicando: "jogador" -> Inicialização: A variável jogador recebe o primeiro elemento da lista. A inicialização só ocorre UMA VEZ ao executar o loop.
                        "in" -> Incremento: Diz como a variável "jogador" muda a cada passo da repetição. O próprio loop cioda para que o próximo elemento seja armazenado na variável.
                        "time" -> O Fim: O teste lógico vai dizer até quando esse loop vai ser executado. O próprio loop cuida do processo de finalizar o loop ao avançar o último elemento da lista.

    FUNÇÕES EM ESTRUTURAS DE REPETÇÃO:

    (RANGE) -> Usada para gerar uma sequência de números inteiros.
               range(início, fim, passo)

               início -> (Opcional)Número inicial da sequência. O padrão é 0.
               fim -> (Obrigatório)Número onde a sequência para (não é incluído)
               passo -> (Opcional)Intervalo entre os números. O padrão é 1. Pode ser negativo.
            
            Exemplo 6: 
             
            %%% Com início %%%
             for i in range(5)
                print(i)
             # Saída: 0 1 2 3 4

             %%% Com início e fim %%%
             for i in range(1, 6):
                print(i)
             # Saída: 1 2 3 4 5

             %%% Com início, fim e passo %%%
             for i in range(10, -1, -2):
                print(i)
             #Saída: 10 8 6 4 2 0
    

    (ENUMERATE) -> Iterar sobre uma sequência (lista ou tupla) ao mesmo tempo em que obtém: o índice (posição do item).
                   Sintaxe: enumerate(iterável, start=0):
                   Explicando: "iterável" -> lista, tupla, string.
                                "start(opcional)" -> valor inicial do índice (padrão é 0).
                
                   Exemplo 7: 
                    
                    nomes = ["Goku", "Vegeta", "Gohan"]

                    for i, nome in enumerate(nomes):                        or              for i, nome in enumerate(nomes, start=1):
                        print(f"{i}:{nome}")                                                   print(f"{i}.{nome}")    


>> Controle de Fluxo <<
  Alterar o comportamento dentro de loops ou blocos.
  #Chaves: break, continue, pass

(BREAK) -> Interrompe imediatamente o loop atual.
           Dentro de laços for ou while
           Sai do loop e continua a execução após o bloco.
           Exemplo 8: 

           for numero in range(10):
               if numero == 7:
                  break #Sai do loop quando encontra o número 7
                print(numero)


(CONTINUE) -> Pula a iteração atual do loop
              Dentro de laços for ou while
              Ignora o restante da iteração atual e passa para a proxima.
              Exemplo 9:

              for numero in range(10):
                if numero == 5:
                    continue #Ignora o número 5
                print(numero)



(PASS) -> Comando vazio que não executa ação alguma.
          Qualquer bloco onde é necessário código sintático.
          Mantém o bloco válido sem alterar o fluxo.
          Exemplo 10:

          def funcao_futura():
            pass #Implementação futura aqui



"""
