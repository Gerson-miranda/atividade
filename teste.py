def celsius_to_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit."""
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius."""
    celsius = (fahrenheit - 32) / 1.8
    return celsius

def main():
    escolha = input("Digite 'C' para converter de Celsius para Fahrenheit ou 'F' para converter de Fahrenheit para Celsius: ").strip().upper()
    
    if escolha == 'C':
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {resultado:.2f}°F")
        
    elif escolha == 'F':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {resultado:.2f}°C")
        
    else:
        print("Escolha inválida. Por favor, digite 'C' ou 'F'.")

if __name__ == "__main__":
    main()

# def encontrar_maior(valor1, valor2, valor3):
#     # Inicialmente assume que valor1 é o maior
#     maior = valor1
    
#     # Verifica se valor2 é maior que o maior atual
#     if valor2 > maior:
#         maior = valor2
    
#     # Verifica se valor3 é maior que o maior atual
#     if valor3 > maior:
#         maior = valor3
    
#     # Imprime o maior valor encontrado
#     print(f"O maior valor é: {maior}")

# # Solicita que o usuário insira os três valores
# try:
#     valor1 = float(input("Digite o primeiro valor: "))
#     valor2 = float(input("Digite o segundo valor: "))
#     valor3 = float(input("Digite o terceiro valor: "))

#     # Chama a função para encontrar e imprimir o maior valor
#     encontrar_maior(valor1, valor2, valor3)
# except ValueError:
#     print("Por favor, insira valores numéricos válidos.")