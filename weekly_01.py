

#Semana 1 - Iacc - Programacion avanzada (Mon 13 Abril 2026)

#Variables a usar
valor_base = 35000
total_ventas_dia = 0

#1. Preguntamos cuantos clientes se procesaran
cantidad_clientes = int(input("👨 Ingrese la cantidad de clientes: "))


for i in range(cantidad_clientes):
    print(f"\n Cliente {i + 1} \n")

    #2. Preguntamos la cantidad de llantas por cliente
    cant_llantas = int(input("🚗 Ingrese la cantidad de llantas: "))


    #3. Logica de precios

    #Si, compra menos de 5 llantas
    if cant_llantas >= 5:
        valor_unidad_llanta = 40000

   #Si, compra 5 a mas de 10 llantas
    elif cant_llantas >= 10:
        valor_unidad_llanta = 45000

    #Si, compra menos de 5 llantas
    else:
        valor_unidad_llanta = valor_base
    
    #guardando y sacando resultado
    total_cliente = cant_llantas * valor_unidad_llanta

    #
    total_ventas_dia += total_cliente

    #imprimiendo resultado
    print(f"- Valor por unidad: ${valor_unidad_llanta}")
    print(f"- Total a pagar por este cliente: ${total_cliente}")
    

#4. Resulta final de la jornada
print("\n 💰 Resumen del dia ")
print(f"----- Total recaudado: ${total_ventas_dia} clientes: {cantidad_clientes}")




