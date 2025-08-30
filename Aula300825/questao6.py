#Duas empresas do mercado de pequenos reparos domésticos determinam o valor de seus serviços a partir de um valor fixo acrescido de um valor cobrado por hora. A empresa X cobra R$ 60,00 de valor fixo mais R$ 18,00 por hora de serviço prestado. A empresa Y cobra R$ 24,00 de valor fixo e está definindo um novo valor a ser cobrado por hora. Sua estratégia de mercado prevê que, em relação à empresa X, o custo total do serviço deve ser menor ou igual para trabalhos de até duas horas de duração. Elabore um programa em Python que simule essa situação, mostrando o valor máximo, em real, que a empresa Y poderá cobrar por hora de serviço prestado a fim de atender à sua estratégia de mercado.

valor_fixo_x = 60.00
valor_hora_x = 18.00
valor_fixo_y = 24.00
print("CALCULADORA DE PREÇO POR HORA")
print(f"Empresa X: R$ {valor_fixo_x} (fixo) + R$ {valor_hora_x} por hora")
print(f"Empresa Y: R$ {valor_fixo_y} (fixo) + ? por hora")
print()


print("ANÁLISE PARA DIFERENTES DURAÇÕES:")
for horas in [1, 2]:
    custo_x = valor_fixo_x + (valor_hora_x * horas)
    valormaxhora= (custo_x - valor_fixo_y) / horas
    print(f"Para {horas} hora(s) de trabalho:")
    print(f" Custo Empresa X: R$ {custo_x:.2f}")
    print(f" Valor máximo/hora Empresa Y: R$ {valormaxhora:.2f}")
    custo_com_valormax = valor_fixo_y + (valormaxhora * horas)
    print(f" Custo Empresa Y (com valor máximo): R$ {custo_com_valormax:.2f}")
    print()


print("RESULTADO FINAL:")
valor_max_1h = (valor_fixo_x + valor_hora_x * 1 - valor_fixo_y) / 1
valor_max_2h = (valor_fixo_x + valor_hora_x * 2 - valor_fixo_y) / 2
valor_maximo_final = min(valor_max_1h, valor_max_2h)
print(f"O valor máximo que a Empresa Y pode cobrar por hora é: R$ {valor_maximo_final:.2f}")
print()


print("SIMULAÇÃO COM O VALOR ENCONTRADO:")
for horas in [1, 2]:
    custo_x = valor_fixo_x + (valor_hora_x * horas)
    custo_y = valor_fixo_y + (valor_maximo_final * horas)
    print(f"{horas} hora(s): Empresa X = R$ {custo_x:.2f} | Empresa Y = R$ {custo_y:.2f}")
    if custo_y <= custo_x:
        print(f"Empresa Y está competitiva (diferença: R$ {custo_x - custo_y:.2f})")
    else:
        print(f"Empresa Y está mais cara!")
    print()