"""
Introdução à Programação em Python

** CARACTERÍSTICAS **
- Simples e de fácil leitura
- Multiplataforma
- Interpretada
- Multiparadigma (suporta programação orientada a objetos, funcional, etc.)
- Tipagem dinâmica
- Grande biblioteca padrão
- Extensível e integravel com outras linguagens
- Comunidade ativa e ecossistema rico.

** AMBIENTE **
- Interpretador Python: Permite executar código Python interativamente.
- IDEs (Integrated Development Environments): Ambientes de desenvolvimento integrados local ou virtual.
- Salvar o código com a extensão .py 

** COMENTÁRIOS **
- Comentários de linha única: Utilizam o símbolo #.
- Comentários de múltiplas linhas: Utilizam três aspas simples ou duplas.

** VARIÁVEIS E CONSTANTES **
- Variáveis: Armazenam valores que podem ser alterados durante a execução do programa.
- REGRAS PARA NOMEAR VARIÁVEIS:
  - Devem começar com uma letra ou um sublinhado (_).
  - Podem conter letras, números e sublinhados.
  - Não podem conter espaços ou caracteres especiais.
  - Não podem ser palavras reservadas do Python (como if, for, while, etc.).
  - São sensíveis a maiúsculas e minúsculas ("variavel" e "Variavel" são diferentes).

- Constantes: Armazenam valores que não podem ser alterados durante a execução do programa.
- Em Python, não há uma sintaxe específica para definir constantes, mas é comum usar letras maiúsculas para indicar que um valor é constante (ex: PI = 3.14).

** TIPOS DE DADOS **
- Tipos de dados básicos: int (inteiro), float (ponto flutuante), str (string), bool (booleano). Exemplo 1 de variáveis e tipos de dados.
- Para verificar o tamanho dos dados usamos a função getsizeof() do módulo sys, que retorna o tamanho em bytes de um objeto. Exemplo 2.
- Para testar o tipo de uma variável, usamos a função type(), que retorna o tipo do objeto. Exemplo 3.
- Para converter um tipo de dado em outro, usamos as funções de conversão, como int(), float(), str(), bool(), etc. Exemplo 4.
- Strings podem ser concatenadas usando o operador +, e podem ser formatadas usando f-strings ou o método format(). Exemplo 5.

** COMANDOS ÚTEIS PARA STRINGS **
- len(): Retorna o comprimento de uma string. Exemplo 6.
- lower(): Converte uma string para minúsculas. Exemplo 7.
- upper(): Converte uma string para maiúsculas. Exemplo 8.
- strip(): Remove espaços em branco do início e do fim de uma string. Exemplo 8.
- split(): Divide uma string em uma lista de substrings com base em um delimitador. Exemplo 9.
- replace(): Substitui ocorrências de uma substring por outra. Exemplo 10.
- find(): Retorna o índice da primeira ocorrência de uma substring. Exemplo 11.
- in: Verifica se uma substring está presente em uma string. Exemplo 12.

"""

# Exemplo 1 de variáveis e tipos de dados

idade = 25  # Variável do tipo inteiro (int)
altura = 1.75  # Variável do tipo ponto flutuante (float)
nome = "Alice"  # Variável do tipo string (str)
maior_de_idade = True  # Variável do tipo booleano (bool)

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Maior de idade:", maior_de_idade)


# Exemplo 2 de uso da função getsizeof() do módulo sys

import sys

print("Tamanho da variável 'idade':", sys.getsizeof(idade), "bytes")
print("Tamanho da variável 'altura':", sys.getsizeof(altura), "bytes")


# Exemplo 3 de uso da função type()
print("Tipo da variável 'nome':", type(nome))
print("Tipo da variável 'maior_de_idade':", type(maior_de_idade))


# Exemplo 4 de uso das funções de conversão
numero_str = "123"
numero_int = int(numero_str)  # Converte a string para inteiro
print("Número convertido para inteiro:", numero_int)
print("Tipo da variável 'numero_int':", type(numero_int))


# Exemplo 5 de concatenação e formatação de strings
sobrenome = "Smith"
nome_completo = nome + " " + sobrenome  # Concatenando strings
print("Nome completo:", nome_completo)


# Exemplo 6 de uso da função len()
print("Comprimento do nome completo:", len(nome_completo))

# Exemplo 7 de uso da função lower()
print("Nome completo em minúsculas:", nome_completo.lower())

# Exemplo 8 de uso da função upper()
print("Nome completo em maiúsculas:", nome_completo.upper())

# Exemplo 9 de uso da função split()
palavras = nome_completo.split(" ")
print("Palavras do nome completo:", palavras)

# Exemplo 10 de uso da função replace()
nome_completo_atualizado = nome_completo.replace("Alice", "Bob")
print("Nome completo atualizado:", nome_completo_atualizado)

# Exemplo 11 de uso da função find()
indice = nome_completo.find("Smith")
print("Índice da ocorrência de 'Smith':", indice)

# Exemplo 12 de uso do operador in
if "Smith" in nome_completo:
    print("O sobrenome 'Smith' está presente no nome completo.")
