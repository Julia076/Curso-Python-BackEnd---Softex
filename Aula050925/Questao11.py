# 11) Elabore um programa que faça os valores da L1 irem para L2 :
L1 = [2, 5, 8, 6, 4]
L2 = [10, 3, 12, 7, 11]
i = 0
while i < len(L1):
    temp = L1[i]
    L1[i] = L2[-(i+1)]
    L2[i] = temp
    i += 1
print(f'Lista 1 final:', L1)
print(f'Lista 2 final:', L2)