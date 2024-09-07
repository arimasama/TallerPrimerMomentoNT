# Definimos una lista con los datos de los pacientes
pacientes = [
    {'nombre': 'Paciente1', 'peso': 70, 'nivel_leucemia': 5},
    {'nombre': 'Paciente2', 'peso': 65, 'nivel_leucemia': 15},
    {'nombre': 'Paciente3', 'peso': 80, 'nivel_leucemia': 45},
    {'nombre': 'Paciente4', 'peso': 75, 'nivel_leucemia': 55},
    {'nombre': 'Paciente5', 'peso': 85, 'nivel_leucemia': 80},
    {'nombre': 'Paciente6', 'peso': 68, 'nivel_leucemia': 25},
    {'nombre': 'Paciente7', 'peso': 77, 'nivel_leucemia': 35},
    {'nombre': 'Paciente8', 'peso': 72, 'nivel_leucemia': 60},
    {'nombre': 'Paciente9', 'peso': 74, 'nivel_leucemia': 90},
    {'nombre': 'Paciente10', 'peso': 69, 'nivel_leucemia': 10}
]

# Función para clasificar el nivel de leucemia
def clasificar_leucemia(nivel):
    if nivel < 10:
        return 'No tiene Leucemia'
    elif 10 <= nivel <= 40:
        return 'Nivel bajo de Leucemia'
    elif 41 <= nivel <= 69:
        return 'Nivel moderado de Leucemia'
    elif 70 <= nivel <= 100:
        return 'Nivel grave de Leucemia'
    else:
        return 'Nivel fuera de rango'

# Recorremos la lista de pacientes y mostramos la clasificación de leucemia
for paciente in pacientes:
    nombre = paciente['nombre']
    nivel_leucemia = paciente['nivel_leucemia']
    clasificacion = clasificar_leucemia(nivel_leucemia)
    
    print(f"Nombre: {nombre}")
    print(f"Nivel de Leucemia: {nivel_leucemia}")
    print(f"Clasificación: {clasificacion}")
    print("-----")
