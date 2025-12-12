CREATE DATABASE IF NOT EXISTS protutoria;
USE protutoria;
CREATE TABLE professores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(20) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    disciplina VARCHAR(50) NOT NULL,
    UNIQUE KEY unique_matricula (matricula)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO professores (matricula, nome, disciplina) VALUES
('MAT001', 'Ana Silva Santos', 'Matemática'),
('POR001', 'Carlos Eduardo Lima', 'Língua Portuguesa'),
('FIS001', 'Maria Fernanda Costa', 'Física'),
('QUI001', 'João Pedro Oliveira', 'Química'),
('BIO001', 'Juliana Rodrigues', 'Biologia'),
('HIS001', 'Roberto Carlos Souza', 'História'),
('GEO001', 'Patricia Almeida', 'Geografia'),
('ING001', 'Michael Anderson', 'Inglês'),
('MAT002', 'Fernando Henrique Dias', 'Matemática'),
('POR002', 'Beatriz Martins', 'Língua Portuguesa');

SELECT * FROM professores;
SELECT * FROM professores WHERE disciplina = 'Matemática';
SELECT disciplina, COUNT(*) as total_professores 
FROM professores 
GROUP BY disciplina 
ORDER BY total_professores DESC;
SELECT * FROM professores WHERE matricula = 'MAT001';
