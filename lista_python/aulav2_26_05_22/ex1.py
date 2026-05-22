# Crie um programa para ler cinco notas de um aluno (usuário/input) e calcule a sua média

def calcula_media(l : list):
    acumulador = 0
    for item in l:
        acumulador += item

    return (acumulador/len(l))

notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = calcula_media(notas)
print(f"A média do aluno é: {media}")

print("---------semfunção---------")

# Sem função

notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

acumulador = 0
for item in notas:
    acumulador += item

media = acumulador / len(notas)
print(f"A média do aluno é: {media}")

print("---------jeitodothomaz---------")

# Jeito do Thomaz

def calcula_media(L : list):
    acc = 0
    for item in L:
        acc += item
    return (acc/len(L))

notas = [0, 0, 0, 0, 0]

for i in range(5):
    notas[i] = float(input(f"Digite a nota {i+1}: "))

print(f"Notas: {notas}")
print(f"Média: {calcula_media(notas)}")