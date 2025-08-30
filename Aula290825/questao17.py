jogador1 = int(input("Jogador1, digite 0 p/pedra, 1 p/papel ou 2 p/tesoura: "))
jogador2 = int(input("Jogador2, digite 0 p/pedra, 1 p/papel ou 2 p/tesoura: "))

pedra = 0
papel = 1
tesoura = 2

if (0 <= jogador1 <= 2) and (0 <= jogador2 <= 2):
    if jogador1 == jogador2:
        print("Empate! Ninguém ganhou.")
    elif (jogador1 - jogador2 == -2) or (jogador1 - jogador2 == 1):
        print("Jogador 1 ganhou.")
    else:
        print("Jogador 2 ganhou.")
else:
    print("Opção inválida.")
