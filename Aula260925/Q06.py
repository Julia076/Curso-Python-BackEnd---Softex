# 06.Elabore um programa em Python que calcule a área de um trapézio qualquer e imprima na tela o resultado.

def calcular_area_trapezio(basemaior, basemenor, altura):
    area = ((basemaior + basemenor) * altura) / 2
    return area
try:
    basemaior = float(input("Digite o valor da base maior: "))
    basemenor = float(input("Digite o valor da base menor: "))
    altura = float(input("Digite o valor da altura: "))

    area = calcular_area_trapezio(basemaior, basemenor, altura)
    print(f"A área do trapézio é: {area}")

except ValueError:
    print("Por favor, digite apenas números válidos.")
