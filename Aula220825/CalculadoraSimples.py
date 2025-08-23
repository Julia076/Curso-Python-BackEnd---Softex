def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Escolha a operação ( +, -, *, /): ")

        match operacao:
            case "+":
                resultado = num1 + num2
                print(f"{num1} + {num2} = {resultado}")
                print(f"A soma é {resultado}")
            case "-":
                resultado = num1 - num2
                print(f"{num1} - {num2} = {resultado}")
                print(f"A subtração é {resultado}")
            case "*":
                resultado = num1 * num2
                print(f"{num1} * {num2} = {resultado}")
                print(f"A multiplicação é {resultado}")
            case "/":
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"{num1} / {num2} = {resultado}")
                    print(f"A divisão é {resultado}")
                else:
                    print("Divisão por zero!")
            case _:
                print("Operação inválida!")

    except ValueError:
        print("Por favor, insira números válidos.")


calculadora()
