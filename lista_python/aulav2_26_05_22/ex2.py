notas = []                                        # Cria uma lista vazia para armazenar as notas
for i in range(5):                                # Loop para ler 5 notas do usuário
    nota = float(input(f"Digite a nota {i+1}: ")) # Solicita ao usuário que digite uma nota e converte para float
    notas.append(nota)                            # Adiciona a nota digitada à lista de notas
acumulador = 0                                    # Inicializa um acumulador para somar as notas

for nota in notas:               # Loop para iterar sobre cada nota na lista de notas
    acumulador += nota           # Adiciona a nota atual ao acumulador
media = acumulador / len(notas)  # Calcula a média dividindo o acumulador pelo número de notas (tamanho da lista)
print(f"Média: {media}")         # Imprime a média calculada

if media >= 6.0:                 # Verifica se a média é maior ou igual a 6.0
    print("Aluno aprovado")      # Imprime que o aluno está aprovado
elif media >= 3.0:
    print("Aluno pode fazer a prova final")    # Imprime que o aluno pode fazer a prova final
else:    
    print("Aluno reprovado direto")            # Imprime que o aluno está reprovado direto
