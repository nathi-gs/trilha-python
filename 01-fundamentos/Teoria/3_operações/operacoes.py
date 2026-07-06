""" 
** Operações de Manipulação de Dados **
Este módulo apresenta exemplos de operações de manipulação de dados em Python, incluindo operações aritméticas, comparação, lógicas e de atribuição.

** OPERAÇÕES ARITMÉTICAS **
'+' - Adição  
Ex: 5+3 = 8

'-' - Subtração 
Ex: 5-3 = 2

'*' - Multiplicação 
Ex: 5*3 = 15

'/' - Divisão 
Ex: 5/3 = 1.666...

'//' - Divisão inteira 
Ex: (5//3 = 1)

'%' - Módulo (resto da divisão)  
Ex: (5%3 = 2)

'**' - Exponenciação 
Ex: (5**3 = 125)


** OPERAÇÕES RELACIONAIS DE COMPARAÇÃO **

'==' - Igual a
Ex: 5 == 3

'!=' - Diferente de
Ex: 5 != 3

'>' - Maior que
Ex: 5 > 3

'<' - Menor que
Ex: 5 < 3

'>=' - Maior ou igual a
Ex: 5 >= 3

'<=' - Menor ou igual a
Ex: 5 <= 3

** OPERAÇÕES LÓGICAS **
'and' - E lógico
Ex: (5 > 3) and (2 < 4)  # Retorna  True

'or' - Ou lógico
Ex: (5 > 3) or (2 > 4)  # Retorna True

'not' - Negação lógica
Ex: not (5 > 3)  # Retorna False

"""

a = 10
b = 5

# Operações aritméticas
print("Adição:", a + b)  # 15
print("Subtração:", a - b)  # 5
print("Multiplicação:", a * b)  # 50
print("Divisão:", a / b)  # 2.0
print("Divisão inteira:", a // b)  # 2
print("Módulo:", a % b)  # 0
print("Exponenciação:", a ** b)  # 100000

# Operações de comparação
print("Igual a:", a == b)  # False
print("Diferente de:", a != b)  # True
print("Maior que:", a > b)  # True
print("Menor que:", a < b)  # False
print("Maior ou igual a:", a >= b)  # True
print("Menor ou igual a:", a <= b)  # False

# Operações lógicas
print("E lógico:", (a > b) and (b > 0))  # True
print("Ou lógico:", (a > b) or (b < 0))  # True
print("Negação lógica:", not (a > b))  # False











