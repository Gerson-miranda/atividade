def verifica_par (numeros):
    contador = 0
    for andar in numeros:
         if (andar%2==0):
             contador +=1
    return contador
numeros = []  
for x in range(6):
    n = int(input(f'digite o numero {x + 1}:'))
    numeros.append(n)
    
print(f'a quantidade de pares é {verifica_par(numeros)}')