def calcular_preco_aluguel (dias,km_percorrido):
    preco_por_dia = 60.00
    preco_por_km = 0.15
    
    custo_total =  (dias * preco_por_dia) + (km_percorrido +preco_por_km)

    return custo_total
dias = int(input('digite a quantidade de dias pelos quais o carro foi alugado : '))

km_percorrido = int(input('digite a quantidae de km percorridos com o carro : '))

preco_a_pagar = calcular_preco_aluguel(dias,km_percorrido)

print(f'o preço a pagar pelo aluguel do carro é R$ { preco_a_pagar :.2f}')