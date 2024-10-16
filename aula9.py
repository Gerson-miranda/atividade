def remove_vogais(texto):
    vogais = ' aeiouAEIOU'
    resultado = ''
    
    for x in texto:
        if x not in vogais:
           resultado += x
    print(f'a quantidade de vogais é {resultado}')        

texto = input('digite algum texto:')

remove_vogais(texto)