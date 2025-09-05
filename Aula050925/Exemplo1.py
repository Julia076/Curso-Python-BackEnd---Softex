nomes=[]

while (True):
    nome=input('Digite um nome, ou x para sair:')
    nome=nome.capitalize() # pegar a primeira letra da palavra digitada e tornar ela em maiuscula 
    if(nome=='x'):
        break 

    print('pertenço ao if')
    nomes.append(nome)
    print(f'os nomes digitador foram {nomes}')

