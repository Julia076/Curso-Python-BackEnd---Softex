# Desenvolva o Jogo PAR ou ÍMPAR, entre você e a máquina. Em que a máquina vai gerar um número aleatório, e você vai fornecer um valor inteiro positivo.O vencedor vai sair no melhor de três jogadas. Imprima na tela o vencedor e quantas jogadas ganhou. *Você pode utilizar: random.randint(0, 10), antes importe a biblioteca: import random.

import random

Vusuario=0
Vmaquina=0

escolha=input("você escolhe par ou impar(P/I)?").upper
for i in range(3):
    nusuario=int(input("Digite um número inteiro e positivo:"))
    nmaquina=random.randint(0,10)
    soma=nusuario+nmaquina

    print(f"Você jogou {nusuario}, Máquina jogou {nmaquina}, soma={soma}")

    if soma % 2 == 0:
        vencedor="P"
    else:
        vencedor="I" 
    if vencedor==escolha:
        print("você venceu essa rodada!")
        Vusuario+=1
    else:
        print("A máquina venceu essa rodada")
print("RESULTADO FINAL")
print(f"você venceu {Vusuario} vez(es)")
print(f"Maquina venceu {Vmaquina} vez(es)")

if Vusuario > Vmaquina:
    print("Você é o grande vencedor!!")
else:
    print(" A maquina venceu!!")
  