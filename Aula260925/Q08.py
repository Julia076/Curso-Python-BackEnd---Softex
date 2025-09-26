# 08. Elabore um programa em Python que calcule a área do quadrado (ABCD)

def calcular_area_quadrado(area_triangulo, base_triangulo):
    altura = (2 * area_triangulo) / base_triangulo
    area_quadrado = altura ** 2
    return area_quadrado

area_triangulo = 12
base_triangulo = 4

resultado = calcular_area_quadrado(area_triangulo, base_triangulo)
print(f"A área do quadrado ABCD é {resultado} cm²")





