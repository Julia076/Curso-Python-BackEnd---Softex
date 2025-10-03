def mais_votado(votos):
    contagem = {}
    for voto in votos:
        if voto in contagem:
            contagem[voto] += 1
        else:
            contagem[voto] = 1

    mais_votado = " "
    maior_voto = 0

    for produto in contagem:
        if contagem[produto] > maior_voto:
            maior_voto = contagem[produto]
            mais_votado = produto

    print("Contagem de votos:", contagem)
    print("Produto mais votado:", mais_votado)

votos = ['A', 'B', 'A', 'C', 'C', 'C', 'A', 'C', 'C', 'B', 'A']
mais_votado(votos)
