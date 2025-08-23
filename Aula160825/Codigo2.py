nome = input("Digite seu nome: ")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido para a idade.")

while True:
    try:
        altura = float(input("Digite sua altura: "))
        break
    except ValueError:
        print("Por favor, digite um número válido para a altura. Use ponto (.) como separador decimal.")

print("\n Dados Informados")
print(f"Meu nome é {nome}")
print(f"Tenho {idade} anos")
print(f"Minha altura é {altura:.2f} metros")
