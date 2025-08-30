#A nota final de um estudante em uma disciplina é dada pela media das notas de suas quatro provas. Cinco estudantes dessa disciplina obtiveram as notas apresentadas no quadro. Com base no texto acima, desenvolva um programa em Python que calcule a nota final e imprima na tela o aluno que teve maior nota final.

def calcular_media(notas):
    total = 0
    for nota in notas:
        total += nota 
    quantidade_notas = 4  
    return total / quantidade_notas
estudantes = []
for i in range(5):
    nome = input(f"Digite o nome do {i+1}º estudante: ")
    notas = []
    print(f"Digite as 4 notas de {nome}:")
    for j in range(4):
        nota = float(input(f"Nota {j+1}: "))
        notas.append(nota)
    estudantes.append({"nome": nome, "notas": notas})
mnota = 0
melhorestudante = ""
for estudante in estudantes:
    media = calcular_media(estudante["notas"])
    if media > mnota:
        mnota = media
        melhorestudante = estudante["nome"]
print(f"\nO aluno com a maior nota final é {melhorestudante} com a nota de {mnota:.2f}")
