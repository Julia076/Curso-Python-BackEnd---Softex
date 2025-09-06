tamanho = int(input("Digite o tamanho da lista: "))
lista = []
for i in range(1, tamanho + 1):
    lista.append(i)
print("Lista gerada:", lista)

ordenada= sorted(lista)
meio = len(ordenada) // 2

if len(ordenada) % 2 != 0:
    mediana = ordenada [meio]
else:
    mediana = (ordenada [meio - 1] + ordenada[meio]) / 2
print("A mediana é:", mediana)
