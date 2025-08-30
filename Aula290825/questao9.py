a=float(input("Digite o primeiro lado: "))
b=float(input("Digite o primeiro lado: "))
c=float(input("Digite o primeiro lado: "))

if(a<b+c) and (b<a+c) and (c<a+b):
    if a == b == c:
        print("Triângulo equilátero!")
    elif a == b or a == c or b == c:
          print("Triângulo isósceles!")
    else:
           print("Triângulo escaleno!")
else:
       print("As medidas NÃO podem formar um triângulo!")
