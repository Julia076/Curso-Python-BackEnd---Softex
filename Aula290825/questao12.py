anos=[]
i=0
while i<3:
    ano=int(input("Digite um ano de nascimento:"))
    anos.append(ano)
    i+=1
    soma=sum(anos)

    print("Anos digitados:", ano)
    print("Soma dos anos:", soma)