from database import get_conexao

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
        self.media = 0
        self.status = ""

    def calcular_media(self):
        self.media = sum(self.notas) / len(self.notas)

    def definir_status(self):
        self.status = "Aprovado" if self.media >= 7 else "Reprovado"

    def salvar(self):
        conexao = get_conexao()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO aluno (nome, nota1, nota2, nota3, nota4, media, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (self.nome, *self.notas, self.media, self.status)
        )

        conexao.commit()
        cursor.close()
        conexao.close()
