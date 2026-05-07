#Semana 3 - Iacc - Programacion avanzada (Viernes 1 Mayor 2026)

#Uso de una Funcion
def frescura_natural():
    print("-- Bienvenido al sistema de inventario Frescura Natural spa --")

    while True:

        #usamos la excepcion try-except para controlar posibles errores de datos
        try:
            #1. Entrada de datos
            existencia = int(input("Ingresa la cantidad actual de productos existentes: "))
            vendidos = int(input("Ingresa la cantidad de productos vendidos el dia de hoy: "))

            #2. Validacion de error
            if existencia < 0 or vendidos < 0:
                print("\n[ERROR] Las cantidades no pueden ser negativas. Inténtelo de nuevo.\n")

                continue

            #Validacion de disponibilidad de stock
            if vendidos > existencia:
                print(f"\n[ERROR] La cantidad vendida ({vendidos}) no puede exceder la existencia ({existencia}).")
                print("Por favor, verifique los datos e intente de nuevo.\n")

                continue

            #procesamiento final si los datos son validos
            stock_final = existencia - vendidos
            
            print("\n" + "="*30)
            print("✅ Registro Exitoso")
            print(f"📦 Ventas del día: {vendidos}")
            print(f"📦 Stock disponible para mañana: {stock_final}")
            
            # --- Aquí van las recomendaciones de textos adicionales ---
            if stock_final == 0:
                print("⚠️  [ALERTA CRÍTICA] ¡Te has quedado sin stock de este producto!")
            elif stock_final < 10:
                print("⚠️  [AVISO] El stock está bajo. Te recomendamos solicitar más productos a la brevedad.")
            else:
                print("✅ [ESTADO] Tienes suficiente stock para operar mañana.")
                
            print("="*30)

            #finaliza el programa con exito
            break 

        except ValueError:
            print("\n[ERROR] Entrada no válida. Por favor, ingrese solo números enteros.\n")


if __name__ == "__main__":
    frescura_natural()