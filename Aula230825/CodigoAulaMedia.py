
n1 = float(input('Informe o 1º valor: '))
n2 = float(input('Informe o 2º valor: '))
n3 = float(input('Informe o 3º valor: '))
n4 = float(input('Informe o 4º valor: '))

media = (n1 + n2 + n3 + n4) / 4


if (media >= 7):
    print("Aluno aprovado!")
elif (media >= 5):
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")
