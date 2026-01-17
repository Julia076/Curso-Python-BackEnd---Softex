import hashlib

def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()
