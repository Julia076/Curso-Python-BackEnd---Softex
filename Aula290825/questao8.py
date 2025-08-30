a=float(input("Digite o primeiro lado: "))
b=float(input("Digite o primeiro lado: "))
c=float(input("Digite o primeiro lado: "))

if(a<b+c) and (b<a+c) and (c<a+b):
    print("As medidas podem formar um triangulo!")
else:
        print("As medidas NÃO podem formar um triangulo!")