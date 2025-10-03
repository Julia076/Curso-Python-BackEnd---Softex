# Faça um programa em Python partindo de uma lista de palavras já inseridas. O código deve ser capaz de encontrar e exibir a maior e menor palavra da lista em número de caracteres. *Use o while ou for para percorrer a lista.

def maior_menor():
    palavras = ["Cachorro", "Gato", "Papagaio", "Leão", "Elefante"]
    
    i = 0
    maior = palavras[0]
    menor = palavras[0]

    while i < len(palavras):
        if len(palavras[i]) > len(maior):
            maior = palavras[i]
        if len(palavras[i]) < len(menor):
            menor = palavras[i]
        i += 1

    print("Maior palavra:", maior)
    print("Menor palavra:", menor)