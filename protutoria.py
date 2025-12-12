
import mysql.connector
def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='protutoria',
            user='root',        # coloque seu usuário
            password=''         # coloque sua senha
        )
        return conexao
    except:
        print("Erro ao conectar no banco!")
        return None

def cadastrar():
    conexao = conectar()
    cursor = conexao.cursor()
    
    print("\n--- CADASTRAR PROFESSOR ---")
    matricula = input("Matrícula: ").upper()
    nome = input("Nome: ")
    disciplina = input("Disciplina: ")
  
    cursor.execute("SELECT * FROM professores WHERE matricula = %s", (matricula,))
    if cursor.fetchone():
        print("Essa matrícula já está cadastrada!")
    else:
        sql = "INSERT INTO professores (matricula, nome, disciplina) VALUES (%s, %s, %s)"
        cursor.execute(sql, (matricula, nome, disciplina))
        conexao.commit()
        print("Professor cadastrado com sucesso!")
    
    cursor.close()
    conexao.close()

def deletar():
    conexao = conectar()
    cursor = conexao.cursor()
    
    print("\n--- DELETAR PROFESSOR ---")
    matricula = input("Digite a matrícula: ").upper()
   
    cursor.execute("SELECT * FROM professores WHERE matricula = %s", (matricula,))
    professor = cursor.fetchone()
    
    if professor:
        print(f"Professor: {professor[2]} - {professor[3]}")
        confirma = input("Tem certeza que quer deletar? (s/n): ")
        
        if confirma.lower() == 's':
            cursor.execute("DELETE FROM professores WHERE matricula = %s", (matricula,))
            conexao.commit()
            print("Professor deletado!")
        else:
            print("Operação cancelada.")
    else:
        print("Professor não encontrado!")
    
    cursor.close()
    conexao.close()

def listar_todos():
    conexao = conectar()
    cursor = conexao.cursor()
    
    print("\n--- LISTA DE PROFESSORES ---")
    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()
    
    if professores:
        for prof in professores:
            print(f"ID: {prof[0]} | Matrícula: {prof[1]} | Nome: {prof[2]} | Disciplina: {prof[3]}")
    else:
        print("Nenhum professor cadastrado.")
    
    cursor.close()
    conexao.close()

def listar_especifico():
    conexao = conectar()
    cursor = conexao.cursor()
    
    print("\n--- BUSCAR PROFESSOR ---")
    matricula = input("Digite a matrícula: ").upper()
    
    cursor.execute("SELECT * FROM professores WHERE matricula = %s", (matricula,))
    professor = cursor.fetchone()
    
    if professor:
        print(f"\nID: {professor[0]}")
        print(f"Matrícula: {professor[1]}")
        print(f"Nome: {professor[2]}")
        print(f"Disciplina: {professor[3]}")
    else:
        print("Professor não encontrado!")
    
    cursor.close()
    conexao.close()

def menu():
    while True:
        print("\n========== SISTEMA PROTUTORIA ==========")
        print("1 - Cadastrar Professor")
        print("2 - Deletar Professor")
        print("3 - Listar Todos")
        print("4 - Buscar Professor")
        print("5 - Sair")
        print("========================================")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            deletar()
        elif opcao == '3':
            listar_todos()
        elif opcao == '4':
            listar_especifico()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
menu()
