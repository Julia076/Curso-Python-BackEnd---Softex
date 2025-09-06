n = int(input("Digite o número de alunos: "))
notas = []
for i in range(n):
    nota = i % 11 
    notas.append(nota)

print("Notas dos alunos:")
for i, nota in enumerate(notas, start=1):
    print(f"Aluno {i}: {nota}")
    
mediageral = sum(notas) / n
acimamedia = 0
for nota in notas:
    if nota > mediageral:
        acimamedia += 1

print(f"Média geral da turma: {mediageral:.2f}")
print(f"Quantidade de alunos com nota acima da média geral: {acimamedia}")

