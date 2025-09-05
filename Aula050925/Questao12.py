alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
palavra = input("Digite a palavra: ").upper()
chave = int(input("Digite a chave: "))
resultado = ''
i = 0
while i < len(palavra):
    letra = palavra[i]
    if letra in alfabeto:
        posiçao = alfabeto.index(letra)
        novaposiçao = (posiçao + chave) % 26
        resultado += alfabeto[novaposiçao]
    else:
        resultado += letra 
    i += 1
print("Criptografado:", resultado)
