"""
**** CLASSE ****

MUNDO
é composto de OBJETOS

OBJETOS
podem ser categorizados 

CLASSE
descreve, de uma maneira abstrata, todos os objetos de uma categoria particular.

** O QUE É UMA CLASSE?
É um projeto de um objeto. Informa como cria um objeto de um tipo específico.
É onde conceituamos o objeto;
Essência do objeto;
Definie os atributos e métodos.

** O QUE É O OBJETO? 
Instância de uma classe.
Objetos semelhantes pertencem a uma mesma classe.

** O QUE É UM ATRIBUTO?
Atributos são as propriedades de um objeto.

** O QUE É MÉTODOS?
Métodos são as ações que um objeto pode realizar.
Exemplo:
- Acelerar
- Frear
- Buzinar

** COMO REPRESENTAMOS UMA CLASSE?
Através da UML (Unified Modeling Language)
Retângulo com três divisões:
-> Nome da Classe;
-> Atributos;
-> Métodos(ações).
Exemplo imagem.

-----------------------------------------------------

**** ATRIBUTOS ****

Tipos de atributos dentro de uma classe:
- Atributos de Instância;
- Atributos de Classe;
- Atributos Estáticos (ou atributos contantes);
- Atributos Dinâmicos.


** ATRIBUTOS DE INSTÂNCIA: 
-> São criados dentro do método __init__ (ou em qualaquer método de instância);
-> Cada objeto(instância) tem sua própria cópia do atributo;
-> São acessados com self.atributo.

Exemplo:

class Pessoa:    #Criando uma classe
    def __init__(self, nome, idade):    #Parâmetros
        self.nome = nome      #atributo de instância
        self.idade = idade    #atributo de instância

class Carro:   
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


** ATRIBUTOS DE CLASSE:
-> Definidos diretamente na classe, fora de qualquer método.
-> Compartilhado entre todas as instâncias da classe;
-> Usados para representar valores comuns a todos os objetos.

Exemplo:

class Livro:
    idioma = "Português"   #atributo de classe

    def __init__(self, titulo):
        self.titulo = titulo      #atributo de instância

class Pessoa:
    contador = 0    #Atributo de classe

    def __init__(self, nome):
        self.nome = nome    #atributo de instância
        Pessoa.contador += 1  #incrementa o contador de classe.


** ATRIBUTOS DE ESTÁTICOS OU CONSTANTES:
-> Atributos de classe que, por convenção, não devem ser alterados;
-> Python não tem constantes reais, mas usa convenção (letras maiúsculas).

Exemplo:

class Config:
    VERSAO = "1.0.0"     #Atributo estático (constante por convenção)
    AUTOR = "Equipe Python"

print(Config.VERSAO)   # 1.0.0
print(Config.AUTOR)    # Equipe Python


** ATRIBUTOS DINÂMICOS:
-> Criados em tempo de execução, adicionando diretamente ao objeto.

Exemplo:

class Animal:
    def __init__(self, especie):
        self.espcie = especie

a = Animal("Cachorro")

# Suponha que recebemos dados externos (ex: de um formulário)

a.nome = "Rex"
a.idade = 5

print(a.nome)   # Rex
print(a.idade)  # 5


class Pessoa:
    def __init__(self, nome): 
        self.nome = nome

p = Pessoa("Ana")
p.sobrenome = "Silva"  # atributo dinâMICO

print(p.sobrenome)     # Silva

-----------------------------------------------------

** SELF

-> self é uma convenção usada para representar a própria instância do objeto dentro dos métodos da classe;
-> É o primeiro parâmetro de todos os métodos (exceto os métodos estáticos).
-> Permite acessar os atributos e outros métodos da mesma instância;
-> Quando chamamos um método de um ojeto, o Python passa automaticamente essa instância como primeiro argumento para o método.

Exemplo:

class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # 'self.nome' é um atributo da instância

    def falar(self):
        print(f"Óla, meu nome é {self.nome}")

p = Pessoa("Ana")
p.falar()      #Python passa automaticamente 'p' como self

"""