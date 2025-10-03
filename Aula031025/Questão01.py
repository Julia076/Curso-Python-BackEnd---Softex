# Desenvolva um programa em Python que imprima na tela em ordem crescente. *Elabore uma função utilizando while e outra utilizando for.
def crescente_while():
    inicio = int(input("Digite o primeiro número: "))
    fim = int(input("Digite o segundo número: "))

    if inicio > fim:
        inicio, fim = fim, inicio

    numero = inicio
    while numero <= fim:
        print(numero)
        numero += 1

 ###############################################################################################################       
def crescente_for():
    inicio = int(input("Digite o primeiro número: "))
    fim = int(input("Digite o segundo número: "))

    if inicio > fim:
        inicio, fim = fim, inicio

    for numero in range(inicio, fim + 1):
        print(numero)
