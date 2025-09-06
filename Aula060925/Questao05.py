numero = int(input("Digite um número inteiro positivo: "))
if numero >= 0:
    for i in range(0, numero + 1):
        if i % 2 == 0:
            print(i)
else:
    print("Você deve digitar um número inteiro positivo.")
