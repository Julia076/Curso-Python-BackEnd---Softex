#Uma imobiliária pôs cinco apartamentos à venda em cinco prédios diferentes de uma cidade brasileira. O quadro apresenta o preço e a área de cada um desses imóveis. Um investidor decidiu comprar o apartamento com o menor preço por metro quadrado dentre os cinco apresentados. Ele deverá comprar o apartamento?

apartamentos = []
for i in range(5):
    print(f"Digite os dados do apartamento {i+1}:")
    preco = float(input("  Preço (R$): "))
    area = float(input("  Área (m²): "))
    precom2= preco / area
    apartamentos.append({
        "numero": i+1,
        "preco": preco,
        "area": area,
        "preco_m2": precom2
    })
print("\nResumo dos Apartamentos:")
for apt in apartamentos:
    print(f"Apartamento {apt['numero']}:")
    print(f"  Preço total: R$ {apt['preco']:.2f}")
    print(f"  Área: {apt['area']} m²")
    print(f"  Preço por m²: R$ {apt['preco_m2']:.2f}\n")
menor_preco = apartamentos[0]["precom2"]
indice_mais_barato = 0

for i in range(1, len(apartamentos)):
    if apartamentos[i]["precom2"] < menor_preco:
        menor_preco= apartamentos[i]["preco_m2"]
        indice_mais_barato = i

mais_barato = apartamentos[indice_mais_barato]
print("APARTAMENTO RECOMENDADO PARA COMPRA:")
print(f"O investidor deve comprar o APARTAMENTO {mais_barato['numero']},")
print(f"que tem o menor preço por m²: R$ {mais_barato['preco_m2']:.2f}")
print(f"Preço total: R$ {mais_barato['preco']:.2f} | Área: {mais_barato['area']} m²")
