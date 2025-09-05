#6) Ler o número de termos da série (n) e imprimir o valor de H, sendo:
n = int(input("Digite o número de termos da série: "))
i = 1
H = 0
while i <= n:
    H = H + 1 / i
    i += 1
print(f"\nValor de H com {n} termos é: {H} ")
