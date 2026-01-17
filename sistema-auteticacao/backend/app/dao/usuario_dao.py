from app.utils.db import get_connection
from app.models.usuario import Usuario

class UsuarioDAO:

    def salvar(self, usuario):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO usuario (nome, email, senha_hash, contato, nivel_graduacao)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            usuario.nome,
            usuario.email,
            usuario.senha_hash,
            usuario.contato,
            usuario.nivel_graduacao
        ))

        conn.commit()
        conn.close()
        return True

    def buscar_por_email(self, email):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM usuario WHERE email = %s", (email,))
        row = cursor.fetchone()

        conn.close()

        if row:
            return Usuario(**row)
        return None
