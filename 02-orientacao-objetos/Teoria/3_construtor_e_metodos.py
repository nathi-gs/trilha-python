"""
******** CONSTRUTOR ********

-> Em python o construtor é um método especial chamado __init__ : 
   Usado para inicializar um objeto assim que ele é criado, definindo os atributos iniciais daquela instância.

-> COMO FUNCIONA O CONSTRUTOR (__init__)
    Quando criamos um objeto(instância) de uma classe, o método __init__ é automaticamente chamado.
    Recebe como primeiro parâmetro o self e outros parâmetros que você definir para inicializar os atributos.

-> Uma classe pode ter apenas um método construtor __init__


******** MÉTODOS ********

-> Funções definidas dentro de classes que operam sobre os dados dos objetos ou da própria classe.
-> Representam os comportamentos que os objetos podem ter.
-> Quando um método é chamado por um objeto, ele pode acessar os atibutos e outros métodos definidos naquela mesma classe.

** TIPOS DE MÉTODOS DENTRO DE CLASSES:
   
   - Métodos de Instância;
   - Métodos de Classe;
   - Métodos Estáticos.


>>>>> MÉTODO DE INSTÂNCIA <<<<<

Opera sobre uma instância específica da classe, ou seja, sobre um objeto criado a partir dela.

-> Características: 
   - O primeiro parâmetro é sempre o self(referência à instância);
   - Pode acessar e modificar atributos do objeto;
   - Pode chmar outros métodos da instância.

-> Quando usar?
   - Quando o comportamento depende dos dados únicos do objeto (atibutos do objeto).



>>>>> MÉTODO DE CLASSE (@classmethod) <<<<<

Opera sobre a própria classe, e não sobre uma instância específica. 
Útil para acessar ou modificar atributos da classe, ou criar métodos de fábrica (que retornam objetos prontos);

-> Características:
   - o primeiro parâmetro é sempre 'cls' (referência à classe);
   - Pode acessar e modificar variáveis da classe;
   - Usa o decorador @classmethod.

-> Quando usar?
   - O comportamento depende da classe como um todo, e não de um objeto específico.



>>>>> MÉTODO ESTÁTICO (@staticmethod) <<<<<





"""