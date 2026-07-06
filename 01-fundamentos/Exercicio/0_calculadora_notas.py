#Calculadora de Notas

nome = input("Digite seu nome: ")
n1 = float(input("Digite sua nota da N1: "))
peso1 = float(input("Digite o pesa da N1: "))
n2 = float(input("Digite sua nota da N2: "))
peso2 = float(input("Digite o pesa da N2: "))
n3 = float(input("Digite a nota da N3: "))
peso3 = float(input("Digite o pesa da N3: "))

nota_final = (n1 * peso1) + (n2 * peso2) + (n3 * peso3) / (peso1 + peso2 + peso3)

print("************ CALCULADORA DE NOTAS ************")
print(f"NOME DO ALUNO: {nome}")
print(f"N1: {n1} possui peso: {peso1}")
print(f"N2: {n2} possui peso: {peso2}")
print(f"N3: {n3} possui peso: {peso3}")
print(f"Média Final: {nota_final}")