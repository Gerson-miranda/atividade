def contar_letras(texto):
    contador = 0
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for x in texto:
        # if x.isalpha():
        if x in alfabeto:
            contador +=1
            
    print(f'a quantidade de letras é {contador}')

texto = input('digite um texto: ')

contar_letras(texto)