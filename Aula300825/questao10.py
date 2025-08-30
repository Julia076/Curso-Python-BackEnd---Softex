# A expressão "relação do ano de nascimento" pode referir-se a várias práticas numerológicas ou astrológicas, como calcular o seu Ano Pessoal (um ciclo de nove anos que descreve as energias para o seu futuro) ou descobrir o seu signo astrológico (baseado no dia e mês do seu nascimento)
# Para calcular o seu Ano Pessoal na Numerologia:
# a. Some os algarismos do seu dia e mês de nascimento. Por exemplo, se nasceu em 15 de junho, some 1 + 5 + 6 = 12
# b. Some os algarismos do ano vigente. Por exemplo, em 2025, some 2 + 0 + 2 + 5 = 9
# c. Some os resultados do dia/mês e do ano. No exemplo: 12 + 9 = 21
# d. Reduza a soma total até um único dígito de 1 a 9. No exemplo: 2 + 1 = 3. Este é o seu Ano Pessoal para aquele ano.


dia = int(input("Digite o dia do seu nascimento (ex: 15): "))
mes = int(input("Digite o mês do seu nascimento (ex: 6): "))
anoatual = int(input("Digite o ano atual (ex: 2025): "))

somadiames = 0
for digito in dia + mes:
    somadiames += int(digito)   

somaano = 0
for digito in anoatual:
    somaano += int(digito)

somatotal = somadiames + somaano
while somatotal > 9:
    novasoma = 0
    for digito in somatotal:
        novasoma += int(digito)
    somatotal = novasoma
print("\nSeu Ano Pessoal é:", somatotal)
print()

if somatotal == 1:
    print("Ano Pessoal 1: é o início de um novo ciclo. Ano de ação, realização e foco em metas.")
elif somatotal == 2:
    print("Ano Pessoal 2: é tempo de explorar relações. Período de equilíbrio e diplomacia.")
elif somatotal == 3:
    print("Ano Pessoal 3: oportunidade para brilhar, usar criatividade e se comunicar.")
elif somatotal == 4:
    print("Ano Pessoal 4: ano de planejamento, esforço e busca por estabilidade.")
elif somatotal == 5:
    print("Ano Pessoal 5: ano de mudanças, adaptação e liberdade.")
elif somatotal == 6:
    print("Ano Pessoal 6: foco em família, comunidade e trabalho em equipe.")
elif somatotal == 7:
    print("Ano Pessoal 7: fase de estudo, reflexão e crescimento pessoal.")
elif somatotal == 8:
    print("Ano Pessoal 8: período de poder, dinheiro, autoridade e sucesso.")
elif somatotal == 9:
    print("Ano Pessoal 9: tempo de fechar ciclos e colher os frutos do que foi plantado.")

