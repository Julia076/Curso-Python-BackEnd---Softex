def mostrarPareseImpares():
    n = int(input("Digite um número inteiro positivo: "))
    
    numero = 0
    while numero <= n:
        if numero % 2 == 0:
            print(numero, "é par")
        else:
            print(numero, "é ímpar")
        numero += 1


