n = int(input("Digite um número inteiro positivo: "))
if n >= 0:
    quadrados_impares = [] 
    for i in range(0, n + 1):
        quadrado = i ** 2
        if quadrado <= n and quadrado % 2 != 0:
            quadrados_impares.append(quadrado)

    # Exibe a lista
    print("Quadrados perfeitos ímpares até", n, ":", quadrados_impares)
else:
    print("Por favor, digite um número inteiro positivo.")
