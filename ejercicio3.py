# Inicializamos las listas para almacenar los números pares e impares
numeros_pares = []
numeros_impares = []

# Pedimos 10 números al usuario
for i in range(10):
    # Solicita un número al usuario
    numero = int(input(f"Ingrese el {i+1}° número: "))
    
    # Determina si el número es par o impar
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)


# Muestra el listado de números pares e impares
print("\nListado de números:")
print(f"Números pares: {numeros_pares} en total son {len(numeros_pares)} números pares")
print(f"Números impares: {numeros_impares} en total son {len(numeros_impares)} números impares")

