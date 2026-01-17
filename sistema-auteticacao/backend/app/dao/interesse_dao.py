from app.utils.db import get_connection
from app.models.interesse import Interesse

class InteresseDAO:

    def listar_por_usuario(self, usuario_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
        SELECT i.id, i.nome
        FROM interesse i
        JOIN usuario_interesse ui ON i.id = ui.interesse_id
        WHERE ui.usuario_id = %s
        """
        cursor.execute(sql, (usuario_id,))
        rows = cursor.fetchall()

        conn.close()

        return [Interesse(**row) for row in rows]
