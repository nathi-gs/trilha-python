""" 
** Entrada e Saída de Dados **
Este módulo apresenta exemplos de como realizar entrada e saída de dados em Python.

** ENTRADA DE DADOS **
A função input() é usada para receber dados do usuário. Ela retorna uma string, então é necessário converter o tipo de dado se for necessário.

** SAÍDA DE DADOS **
A função print() é usada para exibir dados na tela. Ela pode receber múltiplos argumentos e suporta formatação de strings.

** FORMATAÇÃO DE STRINGS **
- f-strings: Permite inserir expressões dentro de strings usando a sintaxe {expressão}. Exemplo: f"Olá, {nome}!".
- Método format(): Permite formatar strings usando chaves {} como marcadores de posição. Exemplo: "Olá, {}!".format(nome).

- Número com casas decimais: :.2f para formatar um número com 2 casas decimais. Exemplo: f"Valor: {valor:.2f}".
- Número inteiro com zeros à esquerda: :05d para formatar um número inteiro com 5 dígitos, preenchendo com zeros à esquerda. Exemplo: f"Número: {numero:05d}".
- Alinhamento de texto: < para alinhar à esquerda, > para alinhar à direita, ^ para centralizar. Exemplo: f"Texto: {texto:<10}" para alinhar à esquerda em um campo de 10 caracteres.

** OPÇÕES DO PRINT () **
- sep: Especifica o separador entre os argumentos. O padrão é um espaço. Exemplo: print("Olá", "Mundo", sep="-")  # Saída: Olá-Mundo
- end: Especifica o que é impresso no final da linha. O padrão é uma nova linha. Exemplo: print("Olá", end=" ")  # Saída: Olá (sem nova linha)
- file: Especifica um objeto de arquivo para onde a saída deve ser direcionada. Exemplo: with open("saida.txt", "w") as f: print("Olá, Mundo!", file=f)  # Escreve "Olá, Mundo!" no arquivo saida.txt

- Quebra de linha: '\n' . Exemplo: print("Linha 1\nLinha 2")  # Saída: Linha 1 (quebra de linha) Linha 2
- Tabulação: '\t' . Exemplo: print("Coluna 1\tColuna 2")  # Saída: Coluna 1 (tabulação) Coluna 2
- Barra invertida: '\\' . Exemplo: print("C:\\Users\\Nome")  # Saída: C:\Users\Nome
- Aspa simples: '\'' . Exemplo: print('Ele disse: \'Olá!\'')  # Saída: Ele disse: 'Olá!'
- Aspa dupla: '\"' . Exemplo: print("Ela disse: \"Oi!\"")  # Saída: Ela disse: "Oi!"
- Backspace: '\b' . Exemplo: print("Olá\b Mundo")  # Saída: Olá Mundo (o \b apaga o 'a' de 'Olá')


"""


# Exemplo 1 de entrada de dados
nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")

# Exemplo 2 de entrada de dados com conversão de tipo
idade_str = input("Digite sua idade: ")
idade = int(idade_str)  # Converte a string para inteiro
print("Você tem " + str(idade) + " anos.")

# Exemplo 3 de saída de dados com múltiplos argumentos
print("Nome:", nome, "Idade:", idade)

# Exemplo 4 de formatação de strings com f-strings
print(f"Olá, {nome}! Você tem {idade} anos.")

# Exemplo 5 de formatação de strings com o método format()
print("Olá, {}! Você tem {} anos.".format(nome, idade))

# Exemplo 6 de formatação de número com casas decimais
valor = 3.14159
print(f"Valor formatado com 2 casas decimais: {valor:.2f}")

# Exemplo 7 de formatação de número inteiro com zeros à esquerda
numero = 42
print(f"Número formatado com zeros à esquerda: {numero:05d}")

# Exemplo 8 de formatação de texto com alinhamento
texto = "Python"
print(f"Texto alinhado à esquerda: {texto:<10}")
print(f"Texto alinhado à direita: {texto:>10}")
print(f"Texto centralizado: {texto:^10}")

# Exemplo 9 de uso do separador e do final do print()
print("Olá", "Mundo", sep="-")  # Saída: Olá-Mundo
print("Olá", end=" ")  # Saída: Olá (sem nova linha)

# Exemplo 10 de uso de caracteres de escape
print("Linha 1\nLinha 2")  # Saída: Linha 1 (quebra de linha) Linha 2
print("Coluna 1\tColuna 2")  # Saída: Coluna 1 (tabulação) Coluna 2
print("C:\\Users\\Nome")  # Saída: C:\Users\Nome
print('Ele disse: \'Olá!\'')  # Saída: Ele disse: 'Olá!'
print("Ela disse: \"Oi!\"")  # Saída: Ela disse: "Oi!"
print("Olá\b Mundo")  # Saída: Olá Mundo (o \b apaga o 'a' de 'Olá')
