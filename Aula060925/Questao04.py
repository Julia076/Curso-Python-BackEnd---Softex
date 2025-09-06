numero = int(input("Digite um número inteiro negativo: "))
if numero < 0:
    for i in range(numero, 1): 
        print(i)
    print(0) 
else:
    print("Você deve digitar um número inteiro negativo.")
