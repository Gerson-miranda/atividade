def combinar_listas_sem_repetidos(lista1, lista2):
    
    lista_combinada = lista1 + lista2
    
    lista_sem_repetidos = list(set(lista_combinada))
    return lista_sem_repetidos

lista1 = [1,2,3,4,5,9,11]
lista2 = [4,5,6,7,8,10,12]

resultado = combinar_listas_sem_repetidos(lista1, lista2)
print("Lista combinada sem elementos repetidos:", resultado)
