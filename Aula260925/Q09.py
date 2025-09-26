# Desenvolva um programa em Python que solicite do usuário um valor inteiro e imprima na tela se o valor digitado é MAIOR, MENOR ou IGUAL A ZERO.

def verificar_valor(numero):
    if numero > 0:
        print("O valor digitado é MAIOR que zero.")
    elif numero < 0:
        print("O valor digitado é MENOR que zero.")
    else:
        print("O valor digitado é IGUAL a zero.")
try:
    valor = int(input("Digite um valor inteiro: "))
    verificar_valor(valor)
except ValueError:
    print("Por favor, digite um número inteiro válido.")

