# a,e,i,o,u
def contar_vogais(texto):
    vogais = ' aeiou'
    contador = 0
    for x in texto:
        if x in vogais:
            contador +=1
    print(f'a quantidade de vogais é {contador}')        

texto = input('digite algum texto:')

contar_vogais(texto)