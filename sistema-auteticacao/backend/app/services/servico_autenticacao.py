from app.dao.usuario_dao import UsuarioDAO
from app.utils.criptografia import criptografar_senha

class ServicoAutenticacao:

    def __init__(self):
        self.usuario_dao = UsuarioDAO()

    def login(self, email, senha):
        usuario = self.usuario_dao.buscar_por_email(email)
        if usuario and usuario.senha_hash == criptografar_senha(senha):
            return usuario
        return None

    def cadastrar(self, usuario):
        usuario.senha_hash = criptografar_senha(usuario.senha_hash)
        return self.usuario_dao.salvar(usuario)
