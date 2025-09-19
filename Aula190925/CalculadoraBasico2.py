def somar(x, y):
  return x + y
def subtrair(x, y):
  return x - y
def multiplicar(x, y):
  return x * y
def dividir(x, y):
  if y == 0:
    return "Divisão por zero não é permitida!"
  return x / y

while True:
    print("\n Calculadora")
    print("1. Adicao")
    print("2. Subtracao")
    print("3. Multiplicacao")
    print("4. Divisao")
    print("5. Sair")

    opcao = input("Escolha uma opção (1-5): ")
    match opcao:
        case '1' | '2' | '3' | '4':
            try:
                a = float(input("Primeiro número: "))
                b = float(input("Segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite números.")
                continue
            match opcao:
                case '1': print(f"{somar(a, b)}")
                case '2': print(f"{subtrair(a, b)}")
                case '3': print(f"{multiplicar(a, b)}")
                case '4': print(f"{dividir(a, b)}")
        case '5':
            print("Saindo.")
            break

        case _:
            print("Opção inválida!!!")