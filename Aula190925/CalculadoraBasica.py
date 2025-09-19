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
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = input("Escolha uma opção (1-5): ")
    if opcao == '5':
        print("Saindo.")
        break
    if opcao in ['1', '2', '3', '4']:
        try:
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
        except:
            print("Entrada inválida.")
            continue
        if opcao == '1':
            resultado = somar(a, b)
        elif opcao == '2':
            resultado = subtrair(a, b)
        elif opcao == '3':
            resultado = multiplicar(a, b)
        else:
            resultado = dividir(a, b)
            print("Resultado:", resultado)
    else:
           print("opção inválida!!!")
            