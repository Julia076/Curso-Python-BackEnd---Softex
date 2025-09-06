numero = int(input("Digite um número inteiro positivo: "))
if numero >= 0:
    quadrados = [] 
    for i in range(0, numero + 1):
        quadrado = i ** 2
        if quadrado <= numero:
            quadrados.append(quadrado)
        else:
            break 
    print("Quadrados perfeitos até", numero, ":", quadrados)

else:
    print("Por favor, digite um número inteiro positivo.")
