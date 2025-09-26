# 10. Crie um programa em Python que solicite do usuário DOIS valores inteiros e imprima na tela qual é o maior deles

def encontrar_maior(valor1, valor2):
    if valor1 > valor2:
        print(f"O maior valor é: {valor1}")
    elif valor2 > valor1:
        print(f"O maior valor é: {valor2}")
    else:
        print("Os dois valores são IGUAIS.")
try:
    numero1 = int(input("Digite o primeiro valor inteiro: "))
    numero2 = int(input("Digite o segundo valor inteiro: "))
    encontrar_maior(numero1, numero2)
except ValueError:
    print("Por favor, digite apenas números inteiros válidos.")
