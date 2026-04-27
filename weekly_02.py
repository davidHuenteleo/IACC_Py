#Semana 2 - Iacc - Programacion avanzada (Mon 20 Abril 2026)

import math

def ejecutar_programa():
    while True:

        #Bienvenida
        print("\n Bienvenido a Software MyPro, revisa nuestras opciones")

        #Opciones
        print("1. Calcula el descuento por compra de licencia")
        print("2. Calcula el volumen de una esfera")
        print("3. Salir")


        #Menu de 3 opciones
        opcion = input("Seleccione una opcion (1, 2 o 3)")


        #Si selecciono la opcion 1 pasa esto:
        if opcion == "1":
            try:
                cantidad = int(input("Ingrese la cantidad de licencias a adquirir: "))
                precio_base = 50000

                if cantidad >= 5:
                    descuento = 0.30000
                elif cantidad >= 3:
                    descuento = 0.20000
                else:
                    descuento = 0.0
                
                precio_final = precio_base * (1 - descuento)
                total_pagar = precio_final * cantidad

                print(f"\n--- Resumen de la compra ---")

                print(f"Precio por licencia con descuento: ${precio_final:.2f}")
                print(f"Total a pagar: ${total_pagar:.2f}")
                print(f"Total a pagar por {cantidad} licencias: ${total_pagar:.2f}")

            except ValueError:
                print("Error: Por favor ingrese un numero valido") 

        #Si selecciono la opcion 2 pasa esto:
        elif opcion == "2":
            try:
                radio = float(input("Ingrese el radio de la esfera, ejemplo: 1.2 : "))
                pi = 3.1416

                #Formula: (4/3) * pi * r^3 
                volumen = (4/3) * pi * (radio ** 3)

                print(f"\n--- Resumen ---")
                print(f"El volumen de la esfera es: {volumen:.2f}")

            except ValueError:
                print("Error: Por favor ingrese un numero valido")

        #Si selecciono la opcion 3 pasa esto:
        elif opcion == "3":
            print("Saliendo del programa... !Hasta Luego")
            break

        else:
            print("Opcion no valida, por favor intente de nuevo")

#Ejecucion del programa
if __name__ == "__main__":
    ejecutar_programa()
