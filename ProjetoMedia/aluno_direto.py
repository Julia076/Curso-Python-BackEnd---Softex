from database import get_conexao

nome = input("Nome do aluno: ")

notas = []
for i in range(1, 5):
    nota = float(input(f"Nota {i}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

status = "Aprovado" if media >= 7 else "Reprovado"

print(f"Média: {media:.2f}")
print(f"Situação: {status}")

conexao = get_conexao()
cursor = conexao.cursor()

sql = """
INSERT INTO aluno (nome, nota1, nota2, nota3, nota4, media, status)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

cursor.execute(sql, (nome, *notas, media, status))
conexao.commit()

cursor.close()
conexao.close()
