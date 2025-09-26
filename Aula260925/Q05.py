# 05. Crie um programa em Python que solicite do usuário três valores e imprima na tela a media desses valores.

def calcularmedia(a, b, c):
    media = (a + b + c) / 3
    return media

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

resultado = calcularmedia(valor1, valor2, valor3)

print(f"A média dos valores é: {resultado}")
