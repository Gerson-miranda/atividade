def verifica(num):
    
    if (num%2==0):
        
        return 'é par'
    
    else:
        return 'é impar'
    
print(verifica(int(input('digite o numero: '))))