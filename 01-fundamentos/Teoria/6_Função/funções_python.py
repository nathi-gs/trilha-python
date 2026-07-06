"""
Funções são blocos de código que executam uma tarefa específica e podem ser reutilizadas.
Sintaxe: Usamos a palavra-chave "def", seguida do nome da função.
         def minha_funcao():
Para chamar uma função basta usar o nome da função seguido de parênteses e seus respectivos parâmetros.
     Exemplo 1: 

        def minha_funcao():
            print("Olá! Esta é uma função simples")
        
        minha_funcao() #chamando a função.

        def saudacao(nome):
            print(f"Olá, {nome}!")
        saudacao("Maria")
        saudacao("João")

Funções também podem retornar um resultado usando a palavra return.
     Exemplo 2:
       
        def soma(a, b):
            return a + b
        
        resultado = soma(3, 5)
        print(resultado)
        8 #Resultado no terminal
    
Apesar de não exigir a função main(), é comum usá-la para organizar o código.
Podemos definir uma função chamada main() e chamá-la usando o seguinte padrão:
Exemplo 3:

def main():
    print("Este é o início do programa.")

#Isso garante que a main só será executada se o script for rodado diretamente.
if __name__ == "__main__":  # Verificação condicional | Ela pergunta: "Este arquivo está sendo executado diretamente pelo usuário?"
    main()                  # Se sim, o python executa o que está dentro do if.
                            # Se não, o código dentro do if não será executado automaticamente.

Explicando: "__name__"  -> é uma variável interna que o python cria automaticamente em cada arquivo que é executado ou importado.
             Se o arquivo está sendo executado diretamente __name__ sera igual a "__main__"
             Se o arquivo está sendo importado como módulo, __name__ será igual ao nome do arquivo (sem .py).

A palavra-chave "import" é usada para trazer código de outro módulo(arquivo) para o programa atual.
#Um módulo em python é um arquivo .py que contém código (funções, variáveis. etc.).

Exemplo 4:

import math
print(math.sqrt(25))
5.0 #Resposta no terminal

Exemplos de sintaxe do import:

** import math  -> Importa o módulo todo
** from math import sqrt -> Importa só a função sqrt
** from math import * -> Importa TUDO do módulo
** import math as m -> Importa com um nome abreviado

"""

print("Exemplo 1: ") 

def minha_funcao():
    print("Olá! Esta é uma função simples")

minha_funcao() #chamando a função.

print("_______________________________________\n")

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Maria")
saudacao("João")

print("_______________________________________\n")

print("Exemplo 2: ")
       
def soma(a, b):
    return a + b
        
resultado = soma(3, 5)
print(resultado)

print("_______________________________________\n")

print("Exemplo 3: ")

def main():
    print("Este é o início do programa.")

#Isso garante que a main só será executada se o script for rodado diretamente.
if __name__ == "__main__":
    main()

print("_______________________________________\n")

print("Exemplo 4: ")
print("Importando biblioteca math e usando a função sqrt()")
import math
print(math.sqrt(25))