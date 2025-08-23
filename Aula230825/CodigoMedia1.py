def ler_nota(numero_nota):
 while True:
        try:
            nota = float(input(f'Informe a {numero_nota}º nota (0 a 10): '))
            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")

n1 = ler_nota(1)
n2 = ler_nota(2)
n3 = ler_nota(3)
n4 = ler_nota(4)

media = (n1 + n2 + n3 + n4) / 4
print(f'\nMédia: {media:.2f}')

if media >= 7:
    print("Aluno aprovado! Com média {media}")
elif media >= 5:
    print("Aluno em recuperação, com média {media}.")
else:
    print("Aluno reprovado, com média {media}")