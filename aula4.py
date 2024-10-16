def encontre_maior_valor(n1,n2,n3):
     maior = 0
     
     if(n1>n2 and n1>n3):
         maior = n1
         
     elif(n2>n1 and n2>n3):
          maior = n2
         
     elif(n3>n2 and n3>n1):
           maior = n3     
         
     print(f'o maior numero é {maior}') 
        
n1 = int(input('digite o primeiro numero:'))
n2 = int(input('digite o segundo numero:'))
n3 = int(input('digite o terceiro numero:'))

encontre_maior_valor(n1,n2,n3)