lista = []

while True:
    print('1- Adicionar item:')
    print('2- Remover item:')
    print('0- Sair:')

    opcao = input("Escolha: ")

    if opcao == '1':
        item = input("Digite o item para adicionar: ")

        if item:
            lista.append(item)
            print(f"{item} adicionado!")

    elif opcao == '2':
        item = input("Digite o item para remover: ")

        if item in lista:
            lista.remove(item)
            print(f"{item} removido!")

        else:
            print("Item não encontrado!")

    elif opcao == '0':
        print("Saindo")

        break
    else:
        print("Opção inválida!")
