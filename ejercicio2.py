
# Definimos una lista con los datos de los empleados
empleados = [
    {'nombre': 'Empleado 1', 'salario_base': 1500000, 'ventas': 5000000},
    {'nombre': 'Empleado 2', 'salario_base': 1200000, 'ventas': 10000000},
    {'nombre': 'Empleado 3', 'salario_base': 1340000, 'ventas': 25000000},
    {'nombre': 'Empleado 4', 'salario_base': 1600000, 'ventas': 3000000},
    {'nombre': 'Empleado 5', 'salario_base': 4000000, 'ventas': 12000000},
    {'nombre': 'Empleado 6', 'salario_base': 5000000, 'ventas': 7000000},
    {'nombre': 'Empleado 7', 'salario_base': 3500000, 'ventas': 30000000},
    {'nombre': 'Empleado 8', 'salario_base': 4500000, 'ventas': 13000000},
    {'nombre': 'Empleado 9', 'salario_base': 2500000, 'ventas': 9000000},
    {'nombre': 'Empleado 10', 'salario_base': 1900000, 'ventas': 15000000}
]

# Definimos una función para calcular el salario neto
def calcular_salario_neto():
    
    # Recorremos la lista de empleados y calculamos el salario neto para cada uno
    for empleado in empleados:
        nombre = empleado['nombre']
        salario_base = empleado['salario_base']
        ventas = empleado['ventas']
        
        seguridadSocial = salario_base*0.08
        comision = ventas*0.05
        
        salario_neto = salario_base + comision - seguridadSocial
        
        # Imprimimos la información del empleado
        print(f"Nombre: {nombre}")
        print(f"Salario Base: ${salario_base:.2f}")
        print(f"Comisión: ${comision:.2f}")
        print(f"Seguridad Social: ${seguridadSocial:.2f}")
        print(f"Salario Neto: ${salario_neto:.2f}")
        print("-----")

calcular_salario_neto();

