# Definimos una lista con los datos de las cabinas
cabinas = [
    {'id': 1, 'puntaje': 2},
    {'id': 2, 'puntaje': 3},
    {'id': 3, 'puntaje': 4},
    {'id': 4, 'puntaje': 2},
    {'id': 5, 'puntaje': 4},
    {'id': 6, 'puntaje': 3},
    {'id': 7, 'puntaje': 2},
    {'id': 8, 'puntaje': 4},
    {'id': 9, 'puntaje': 3},
    {'id': 10, 'puntaje': 2}
]

# Función para clasificar el funcionamiento de la cabina
def clasificar_funcionamiento(puntaje):
    if puntaje == 2:
        return 'Funcionamiento defectuoso'
    elif puntaje == 3:
        return 'Funcionamiento moderado'
    elif puntaje == 4:
        return 'Funcionamiento óptimo'
    else:
        return 'Puntaje fuera de rango'

# Recorremos la lista de cabinas y mostramos la clasificación de funcionamiento
for cabina in cabinas:
    id_cabina = cabina['id']
    puntaje = cabina['puntaje']
    clasificacion = clasificar_funcionamiento(puntaje)
    
    print(f"ID de Cabina: {id_cabina}")
    print(f"Puntaje: {puntaje}")
    print(f"Clasificación: {clasificacion}")
    print("-----")
