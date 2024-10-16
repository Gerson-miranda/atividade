def celsius_to_fahrenheit(celsius):
    
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    
    celsius = (fahrenheit - 32) /1.8
    return celsius


escolha = input("Digite 'c' para converter de Celsius para Fahrenheit ou 'f' para converter de Fahrenheit para Celsius: ")
    
if escolha == 'c':
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {resultado:.2f}°F")
        
elif escolha == 'f':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {resultado:.2f}°C")
        
else:
        print("Escolha inválida. Por favor, digite 'c' ou 'f'.")