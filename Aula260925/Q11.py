# 11.Faça um programa em Python que solicite do usuário TRÊS valores inteiros e imprima na tela qual é o maior deles.

def encontrar0maior(valor1, valor2, valor3):
    maior = valor1
    if valor2 > maior:
        maior = valor2
    if valor3 > maior:
        maior = valor3
    print(f"O maior valor digitado é: {maior}")
try:
    num1 = int(input("Digite o primeiro valor inteiro: "))
    num2 = int(input("Digite o segundo valor inteiro: "))
    num3 = int(input("Digite o terceiro valor inteiro: "))
    encontrar0maior(num1, num2, num3)
except ValueError:
    print("Por favor, digite apenas números inteiros válidos.")
