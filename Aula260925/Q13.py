def triangulo(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Os segmentos PODEM formar um triângulo.")
    else:
        print("Os segmentos NÃO PODEM formar um triângulo.")
try:
    l1 = float(input("Digite o primeiro segmento de reta: "))
    l2 = float(input("Digite o segundo segmento de reta: "))
    l3 = float(input("Digite o terceiro segmento de reta: "))
    triangulo(l1, l2, l3)
except ValueError:
    print("Por favor, digite números válidos.")
