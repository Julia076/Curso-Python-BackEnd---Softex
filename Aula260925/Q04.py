# 04.Faça um programa em Python que solicite do usuário nome, idade e altura, e imprima na tela: “<nome> tem <idade> e uma altura de <altura> metro.”

def exibir():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    altura = input("Digite sua altura (em metros): ")
    
    print(f"{nome} tem {idade} anos e uma altura de {altura} metro.")

exibir()
