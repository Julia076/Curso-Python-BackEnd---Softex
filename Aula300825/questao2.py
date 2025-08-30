# Faça um código em Python que imprima na tela se uma função polinomial do 2o grau tem ou não solução no conjunto dos números reais, se tiver, imprima o número de solução(ões).f (x) = a2 + bx + c, sendo a ≠ 0 
# * Δ>0 DUAS raízes reais distintas; 
# * Δ=0 UMA raiz real (P.s: x’ = x”);
# * Δ<0 NÃO tem solução nos reais.

def calcular_raizes(a, b, c):
       delta = b**2 - 4*a*c
       if delta > 0:
               x1 = (-b + (delta)**0.5) / (2*a)  
               x2 = (-b - (delta)**0.5) / (2*a)
               print(f"Existem duas raízes reais distintas: x' = {x1} e x'' = {x2}")
       elif delta == 0:
        x = -b / (2*a)
        print(f"Existe uma raiz real: x = {x}")
       else:
               print("Não há soluções reais.")
a = float(input("Digite o valor de a (diferente de 0): "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
calcular_raizes(a, b, c)
