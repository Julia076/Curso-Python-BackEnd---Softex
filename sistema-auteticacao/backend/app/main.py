from app.services.servico_autenticacao import ServicoAutenticacao
from app.models.usuario import Usuario

servico = ServicoAutenticacao()

novo_usuario = Usuario(
    nome="Maria",
    email="maria@email.com",
    senha_hash="123456",
    contato="99999-9999",
    nivel_graduacao="Superior"
)

servico.cadastrar(novo_usuario)

usuario = servico.login("maria@email.com", "123456")

if usuario:
    print("Login realizado com sucesso!")
else:
    print("Falha no login.")
