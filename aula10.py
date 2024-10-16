total_eleitores = int(input('digite o total de eleitores : '))

candidato1 = 0
candidato2 = 0
candidato3 = 0

for x in range(total_eleitores):
    voto = int(input('digite 1 para o candidato 1 - digite 2 para o candidato 2 - digite 3 para o candidato 3:'))
    
    if (voto == 1):
        candidato1 +=1
        
    elif (voto == 2):
        candidato2 +=1
        
    elif (voto == 3):
        candidato3 +=1
        
    else:
        print('voto invalido você votou nulo !! ')
        
print(f'a quantidade de votos do candidato 1: {candidato1} votos')
print(f'a quantidade de votos do candidato 2: {candidato2} votos')
print(f'a quantidade de votos do candidato 3: {candidato3} votos')

if(candidato1>candidato2 and candidato1 > candidato3):
    print(f'o candidato 1 foi o vencedor da eleição !')
    
elif(candidato2>candidato1 and candidato2 > candidato3):
    print(f'o candidato 2 foi o vencedor da eleição !')
    
elif(candidato3>candidato1 and candidato3 > candidato2):
    print(f'o candidato 3 foi o vencedor da eleição !')
    
else:
    print(f'houve empate !!')