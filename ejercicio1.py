# Inicializamos los primeros dos números de la serie
num1 = 5
num2 = 8

# Lista para almacenar la serie
serie = []

# Contador para asegurarnos de obtener 100 números
contador = 0

# Variable para almacenar el nuevo número en cada iteración
nuevo_numero = 0

# Mientras no se hayan calculado 100 números
while contador < 100:
    # Verificamos si el número actual no es 13
    if num1 != 13:
        # Agregamos el número a la lista 'serie'
        serie.append(num1)
        # Incrementamos el contador
        contador += 1
    
    # Calculamos el nuevo número sumando los dos anteriores
    nuevo_numero = num1 + num2
    
    # Actualizamos los valores de num1 y num2 para la próxima iteración
    num1 = num2
    num2 = nuevo_numero

# Mostramos la lista completa de los primeros 100 números
print(serie)
print(len(serie)) #aqui nos muestra cuantos elementos hay en el array
