#Semana 4 - Iacc - Programacion avanzada (Sun 3 may 2026)

#funcion que contiene las listas
def administrador_museo():

    #Se usa listas vacias 
    sala1 = []
    sala2 = []
    sala3 = []


    print("--- Registro de Visitantes del Museo ---")

    #se inicia un ciclo infinito para el registro de los visitantes
    while True:

        nombre = input("\n Ingrese nombre del visitante o salir para finalizar ")

        if nombre.lower() == "salir":
            break

        print(f"¿A que salas ingreso {nombre}?")
        
        # Agregamos .strip() para limpiar si el usuario ingresa espacios en blanco por error antes o después del "si"
        s1 = input("¿Sala 1: (si / no)? ").strip().lower() == "si"
        s2 = input("¿Sala 2: (si / no)? ").strip().lower() == "si"
        s3 = input("¿Sala 3: (si / no)? ").strip().lower() == "si"

        #Registro en salas correspondientes
        if s1: sala1.append(nombre)
        if s2: sala2.append(nombre)
        if s3: sala3.append(nombre)


    # --- FUERA DEL CICLO WHILE ---
    # (Le quitamos la sangría/tabulación para que el reporte se imprima SÓLO cuando se escribe "salir")

    #Aqui obtengo una lista unica de todos los visitantes
    todos_los_visitantes = set(sala1 + sala2 + sala3)
    lista_unica = sorted(list(todos_los_visitantes))

    #Mostrar resultado
    print("\n" + "="*30)
    print("REPORTE DE VISITAS FINAL")
    print("="*30)
    print(f"Visitantes en Sala 1: {sala1}")
    print(f"Visitantes en Sala 2: {sala2}")
    print(f"Visitantes en Sala 3: {sala3}")


    print("\n--- Lista Única de Visitantes (Sin Duplicados) ---")
    for i, visitante in enumerate(lista_unica, 1):
        print(f"{i}. {visitante}")

    #Ejecutar el programa semana 4

administrador_museo()