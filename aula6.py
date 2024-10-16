
def somar(produtos):
    total=sum(produtos)
    print(f'o total vai ser de R$ {total:.2f}')
    
compras=[]
    
while True:
     produtos= float(input('digite o valor dos produtos:'))
     if (produtos== -1):
        break 
     else:
        compras.append(produtos)
somar(produtos) 