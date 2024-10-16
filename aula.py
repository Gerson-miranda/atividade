import random

import os

     
numero_secreto = random.randint(1,100)

tentativas = 0

acertou = False

while not acertou :
    palpite = int(input('chute um número de  1 e 100:'))
    os.system('cls')
    
    tentativas += 1
    
    if (palpite==numero_secreto):
        
        acertou = True
        
        print(f'você acertou o número {numero_secreto} em {tentativas} tentativas ,parabéns!')
        break
    
    elif (palpite>numero_secreto):
        print ('o seu número foi alto . tente novamente .')
    
    else:
        print ('o seu número foi baixo . tente novamente.')