tempos=[]
contador=1
while contador <= 8:
    tempo=float(input(f"digite o tempo do atleta {contador} em segundos:"))
    tempos.append(tempo)
    contador +=1

    n=len(tempos)
if n % 2 == 1:  
        mediana = tempos[n // 2]
else: 
        mediana = (tempos[n // 2 - 1] + tempos[n // 2]) / 2

print(f"Mediana até agora: {mediana:.2f}")