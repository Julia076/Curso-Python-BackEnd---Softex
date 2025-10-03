# 4) Elabore um programa em Python em que calcule a média dos valores (já fornecida). *Utilize o while ou for.
def media_while():
    numeros = [10, 2, 30, 5, 60] 
    soma = 0
    i = 0

    while i < len(numeros):
        soma += numeros[i]
        i += 1

    media = soma / len(numeros)
    print("A média é:", media)
