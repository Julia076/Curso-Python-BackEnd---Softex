CREATE DATABASE sistema_autenticacao;
USE sistema_autenticacao;

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    contato VARCHAR(50),
    nivel_graduacao VARCHAR(50)
);

CREATE TABLE interesse (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE usuario_interesse (
    usuario_id INT,
    interesse_id INT,
    PRIMARY KEY (usuario_id, interesse_id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY (interesse_id) REFERENCES interesse(id)
);
