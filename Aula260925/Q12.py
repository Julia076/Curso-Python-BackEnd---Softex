# 12.  Elabore um programa que informe se um número digitado pelo usuário foi um número par ou ímpar.

def verificar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")
try:
    valor = int(input("Digite um número inteiro: "))
    verificar(valor)
except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")
