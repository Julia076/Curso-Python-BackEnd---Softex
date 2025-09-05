#10) Desenvolva um programa em Python que simule um banco de dados, onde um usuário vai armazenar n nomes e outro usuário vai pesquisar nome de pessoas que iniciam com uma letra qualquer. Deve ser impresso na tela os nomes que começam com a letra fornecida pelo usuário.

nomes = []
i = 0
n = int(input("Quantos nomes deseja armazenar? "))
while i < n:
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome.capitalize()) 
    i += 1
letra = input("Digite uma letra para buscar nomes que comecem com ela: ")
letra = letra.capitalize()
print(f"Nomes que começam com '{letra}':")
i = 0
while i < len(nomes):
      if nomes[i][0] == letra:
        print(nomes[i])
      i += 1
