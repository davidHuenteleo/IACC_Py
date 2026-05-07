#Semana 5 - Iacc - Programacion avanzada (Sun 3 may 2026)

#datetime
from datetime import datetime

#--- Logico del sistema ---
def calculadora_antiguedad(fecha_ingreso):


    hoy = datetime.now()

    #Diferencia basica de años
    antiguedad = hoy.year - fecha_ingreso.year

    #Ajuste si aun no ha pasado el mes/dia del aniversario
    if (hoy.month, hoy.day) < (fecha_ingreso.month, fecha_ingreso.day):
        antiguedad -= 1

    return antiguedad

def determinar_beneficios(antiguedad):

    beneficios = []

    if antiguedad >= 5:
        beneficios.append("Bono anual")

    if antiguedad >= 3:
        beneficios.append("5 dias adicionales de vacaciones")
    
    #Retorna los beneficios unidos por coma o un mensaje si no tienen
    return ", ".join(beneficios) if beneficios else "Ninguno"

def mostrar_reporte_empleado(nombre, edad, salario, fecha_ingreso):

    #calcula 
    anios = calculadora_antiguedad(fecha_ingreso)
    premios = determinar_beneficios(anios)


    #resultado final
    print("\n" + "="*30)
    print("REPORTE DE EMPLEADO")
    print("="*30)

    print(f"Empleado: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Salario: ${salario}")
    print(f"Antigüedad: {anios} años")
    print(f"Beneficios asignados: {premios}")
    
    print("="*30)


# --- INTERFAZ INTERACTIVA ---
print("--- Ingreso de Datos del Empleado ---")
nombre_input = input("Ingrese su nombre: ")
edad_input = input("Ingrese su edad: ")
salario_input = input("Ingrese su salario: ")
anio_ingreso = int(input("Ingrese su año de ingreso (ej. 2018): "))

# Creamos la fecha asumiendo el 1 de enero de ese año para que el cálculo funcione con tu función original
fecha_ingreso_input = datetime(anio_ingreso, 1, 1)

# Llamamos a la función con los datos que ingresó el usuario
mostrar_reporte_empleado(nombre_input, edad_input, salario_input, fecha_ingreso_input)


