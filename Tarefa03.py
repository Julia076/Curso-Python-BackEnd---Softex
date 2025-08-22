p = float(input('informe quanto você aplicou:'))
i = input('informe a taxa:')
n = int(input('informe quantos meses:'))
i = i.replace("%", "")

t = float(i)/100

M = p*(1+t)**n
J = M-p

print(f'Montante: R$ {M:.2f}')
print(f'Rendeu: {J:.2f}')
