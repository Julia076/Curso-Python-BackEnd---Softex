nomes = []
n = int(input("Quantos nomes deseja cadastrar? "))
for i in range(n):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)
letra = input("Digite a letra para pesquisar os nomes que começam com ela: ").capitalize()
print(f"Nomes que começam com '{letra}':")
for nome in nomes:
    if nome[0].capitalize() == letra:
        print(nome)
