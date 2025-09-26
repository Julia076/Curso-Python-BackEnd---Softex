#16.Elabore um programa em Python que simule o jogo PEDRA, PAPEL e TESOURA. Sendo um dos jogadores a máquina e o outro o usuário. Mostre o quem ganhou e a escolha de ambos.
import random

print("Escolha: pedra, papel ou tesoura")
usuario = input("Você: ").lower()
maquina = random.choice(["pedra", "papel", "tesoura"])

print(f"Máquina: {maquina}")

if usuario == maquina:
    print("Empate!")
elif (usuario == "pedra" and maquina == "tesoura") or (usuario == "papel" and maquina == "pedra") or (usuario == "tesoura" and maquina == "papel"):
    print("Você venceu!")
else:
    print("Máquina venceu!")
