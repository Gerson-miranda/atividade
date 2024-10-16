def calcular_media(num1,num2,num3):
    media =(num1+num2+num3)//3
    return media


def resultado(m):
    if(m>=7):
        print('você foi aprovado')
        
    else:
        print('você foi reprovado')
        
num1= float(input('digite a primeira nota : '))
num2= float(input('digite a segunda  nota : '))
num3= float(input('digite a terceira nota : '))

media = calcular_media(num1,num2,num3)    

resultado(media)       
     