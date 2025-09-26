# 14.  Faça um programa em Python que permita calcular o número de diagonais que um polígonoregular, a soma interno e quanto é ângulo interno. O usuário vai fornecer o número de vértices desse objeto.

def calcularpoligono(n):
     if n < 3:
        print("Um polígono precisa ter pelo menos 3 lados.")
        return

     diagonais = (n * (n - 3)) // 2
     somaAI = (n - 2) * 180
     angulo_interno = somaAI / n

     print(f"Número de vértices: {n}")
     print(f"Número de diagonais: {diagonais}")
     print(f"Soma dos ângulos internos: {somaAI}°")
     print(f"Ângulo interno de cada vértice: {angulo_interno}°")

try:
    lados = int(input("Digite o número de lados do polígono regular: "))
    calcularpoligono(lados)
except ValueError:
    print("Por favor, digite um número inteiro válido.")

