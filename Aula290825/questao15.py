def ler_nota(numero_nota):
    while True:
        try:
            nota = float(input(f'Informe a {numero_nota}ª nota (0 a 10): '))
            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")

contador = 1
while contador <= 3:
    print(f'\nNotas do {contador}º aluno:')
    
    n1 = ler_nota(1)
    n2 = ler_nota(2)
    n3 = ler_nota(3)
    n4 = ler_nota(4)

    media = (n1 + n2 + n3 + n4) / 4
    print(f'\nMédia do {contador}º aluno: {media:.2f}')

    if media >= 6:
        print(f"Aluno {contador} aprovado! Com média {media:.2f}")
    elif media >= 4:
        print(f"Aluno {contador} em recuperação, com média {media:.2f}.")
    else:
        print(f"Aluno {contador} reprovado, com média {media:.2f}")

    contador += 1
