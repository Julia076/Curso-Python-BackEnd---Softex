class Usuario:
    def __init__(self, id=None, nome=None, email=None, senha_hash=None, contato=None, nivel_graduacao=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash
        self.contato = contato
        self.nivel_graduacao = nivel_graduacao
