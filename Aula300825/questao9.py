#Desenvolva um programa em Python, em que é fornecido um número inteiro positivo, só que ao ser impresso na tela o mesmo deve ser presentado em algarismos romano. São utilizadas sete letras do alfabeto: Quatro fundamentais: I (vale 1); X (vale 10); C (vale 100) e M (vale 1 000). Três secundárias: V (vale 5); L (vale 50); e D (vale 500). As regras para escrever números romanos são:
# a. Não existe símbolo correspondente ao zero;
# b. Os símbolos fundamentais podem ser repetidos até três vezes e seus valores são adicionados. Exemplo: XXX = 30;
# c. Uma letra posta à esquerda de outra de maior valor indica subtração dos respectivos valores. Exemplo: IX = 10 – 1 = 9;
# d. Uma letra posta à direita de outra de maior valor indica adição dos respectivos valores.

# Exemplo: XI = 10 + 1 = 11

def int_para_romano(numero):

    valores_romanos = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    resultado = ""

    for item in valores_romanos:
        valor = item[0]       
        simbolo = item[1]     

        while numero >= valor:
            resultado += simbolo  
            numero -= valor       
    
    return resultado

num = int(input("Digite um número inteiro positivo: "))

if num <= 0:
    print(" Não existe número romano para zero ou negativos.")
else:
    romano = int_para_romano(num)
    print(f"O número {num} em algarismos romanos é: {romano}")
