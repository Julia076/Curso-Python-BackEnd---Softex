valor = float(input("Digite o total gastos: "))

print("\n Formas de pagamento:")
print("1- à vista com 10% de desconto")
print("2- em duas vezes (preço de etiqueta)")
print("3- de 3 até 10 vezes com 3% de juros ao mês (somente para compras acima de R$ 100,00)")

opcao = int(input("\nEscolha a opção desejada: "))

if opcao == 1:
    total=valor-(valor * 0.10)
    print(f"Valor a pagar R$:{total:.2f}")
elif opcao == 2:
    total = valor
    parcela = valor / 2
    print(f"2 parcelas de R$ {parcela:.2f} (total R$ {total:.2f})")
elif opcao == 3:
    if valor>100:
        vezes = int(input("Digite em quantas vezes (3 a 10): "))
        if 3 <= vezes <= 10:
            total = valor * (1 + 0.03 * vezes)
            parcela = total / vezes
            print(f"{vezes} parcelas de R$ {parcela:.2f} (total R$ {total:.2f})")
        else:
            print("Número de parcelas inválidas!")
    else:
        print("Essa opção é válida somente para compras acima de R$ 100,00.")
else:
    print("Opção inválida!")
