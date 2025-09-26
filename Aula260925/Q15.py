# 15.  Com base na questão anterior, determine caso seja um triângulo, qual é: Triângulo Equilátero, Triângulo Isósceles ou Triângulo Escaleno

def formar_triangulo(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def tipo(a, b, c):
    if a == b == c:
        return "Triângulo Equilátero"
    elif a == b or b == c or a == c:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"

try:
    l1 = float(input("Digite o primeiro segmento de reta: "))
    l2 = float(input("Digite o segundo segmento de reta: "))
    l3 = float(input("Digite o terceiro segmento de reta: "))

    if formar_triangulo(l1, l2, l3):
        tipo = tipo(l1, l2, l3)
        print(f"Os segmentos PODEM formar um triângulo.")
        print(f"Tipo de triângulo: {tipo}")
    else:
        print("Os segmentos NÃO PODEM formar um triângulo.")
except ValueError:
    print("Por favor, digite valores numéricos válidos.")