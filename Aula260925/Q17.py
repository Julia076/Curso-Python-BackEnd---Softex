def verificar_aniversario(dia, mes, diaatual, mesatual):
    if mes < mesatual or (mes == mesatual and dia < diaatual):
        print("Seu aniversário já passou este ano.")
    elif mes == mesatual and dia == diaatual:
        print("Hoje é seu aniversário! Parabéns!")
    else:
        print("Seu aniversário ainda vai chegar este ano.")

dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

diaatual = 26
mesatual = 9

verificar_aniversario(dia, mes, diaatual, mesatual)
