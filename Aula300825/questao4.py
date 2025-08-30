# Um usuário ao invés de fornecer as medidas dos segmento de reta de um triângulo qualquer,ele forneceu três pontos A, B e C. Cada ponto pode ser encontrado pela sua coordenada, exemplo: Com base nessas informações desenvolva um programa em Python que imprima na tela as medidas dos segmentos de retas: AB, BC e CA respectivamente.


def calcular_distancia(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

xA = float(input("Digite a coordenada x de A: "))
yA = float(input("Digite a coordenada y de A: "))
xB = float(input("Digite a coordenada x de B: "))
yB = float(input("Digite a coordenada y de B: "))
xC = float(input("Digite a coordenada x de C: "))
yC = float(input("Digite a coordenada y de C: "))

AB = calcular_distancia(xA, yA, xB, yB)
BC = calcular_distancia(xB, yB, xC, yC)
CA = calcular_distancia(xC, yC, xA, yA)

print(f"Distância AB: {AB:.2f}")
print(f"Distância BC: {BC:.2f}")
print(f"Distância CA: {CA:.2f}")
