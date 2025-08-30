numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o tereiro número inteiro: "))

if numero1 >= numero2 and numero1 >= numero3:
    print("O maior número é:", numero1)
elif numero2 >= numero1 and numero2 >= numero3:
    print("O maior número é:", numero2)
else:
    print("O maior número é:", numero3)