#Construa um programa em Python que imprima na tela os números pares de 0 até n. *Elabore uma função utilizando while e outra utilizando for.

def pares_while():
    n = int(input("Digite um número inteiro: "))
    numero = 0

    while numero <= n:
        if numero % 2 == 0:
            print(numero)
        numero += 1

###############################################################################################################

def pares_com_for():
    n = int(input("Digite um número inteiro: "))

    for numero in range(0, n + 1):
        if numero % 2 == 0:
            print(numero)
