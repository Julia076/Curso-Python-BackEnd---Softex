numero = int(input("Digite um valor inteiro positivo: "))

if numero < 1:
    print("Número inválido! Digite apenas número positivo.")
else:
    if numero % 2 == 0:        
        print("OKOSA " * (numero//2))
    else:
       if(numero > 1):
            print("OKOSA " * (numero//2) + 'URAPUM'*(numero%2))
       else:
          print('URAPUM')


  