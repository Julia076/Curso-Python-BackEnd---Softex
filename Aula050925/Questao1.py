#1) Faça um programa em Python que imprima na tela os dez primeiros números em ordem crescente.
numeros = []
i = 0
while i < 10:
    num = int(input(f'Digite o {i+1}° número: '))
    numeros.append(num)
    i += 1
trocou = True
while trocou:
    trocou = False
    j = 0
    while j < len(numeros) - 1:
        if numeros[j] > numeros[j+1]: 
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
            trocou = True
        j += 1

print("\nNúmeros em ordem crescente:")
print(numeros)
