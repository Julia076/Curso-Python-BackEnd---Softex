# 07. Um terreno no formato quadrangular: L1, L2, L3 e L4 representando os comprimentos desse terreno. Sabendo que 100 metros de arame farpado custa R$ 86,90 e é necessário quatro voltas para cercar o terreno direito. Desenvolva um programa em Python que mostre quanto custa para cercar um terreno. 

def calcularcusto(L1, L2, L3, L4):
    preco100m = 86.90 
    voltas = 4
    perimetro = L1 + L2 + L3 + L4
    totalmetros = perimetro * voltas
    custototal = (totalmetros / 100) * preco100m
    return custototal

L1 = float(input("Digite o comprimento do lado 1 (em metros): "))
L2 = float(input("Digite o comprimento do lado 2 (em metros): "))
L3 = float(input("Digite o comprimento do lado 3 (em metros): "))
L4 = float(input("Digite o comprimento do lado 4 (em metros): "))

custo = calcularcusto(L1, L2, L3, L4)

print(f"O custo total para cercar o terreno é: R$ {custo:.2f}")
