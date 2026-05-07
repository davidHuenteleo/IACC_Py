#Semana 6 - Iacc - Programacion avanzada

import json
import os

#Nombres de los archivos
FILE_BOOKS = "libros.json"
FILE_AUTHORS = "autores.json"


def cargar_datos(archivo):

    #Carga datos desde un archivo JSON. Si no existe, devuelve una lista vacia

    if not os.path.exists(archivo):

        return[]

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    except (json.JSONDecoderError, IOError):
        return[]
    

def guardar_datos(archivo, datos):

#Guarda la lista de datos en el archivo JSON con indentacion 
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
           json.dump(datos, f, indent=4, ensure_ascii=False)

    except IOError as e:
        print(f"Error al guardar los datos: {e}")


def agregar_libro():

    print("\n--- Agregar Nuevo Libro ---")

    titulo = input("Titulo: ")
    genero = input("Genero: ")
    anio = input("Año de publicacion: ")
    autor = input("Nombre del autor: ")


    libros = cargar_datos(FILE_BOOKS)
    nuevo_libro = {
        "titulo": titulo,
        "genero": genero,
        "anio": anio,
        "autor": autor
    }


    libros.append(nuevo_libro)
    guardar_datos(FILE_BOOKS, libros)
    print("\n✔️ ¡Libro agregado con éxito!")


def agregar_autor():
    print("\n--- Agregar Nuevo Autor ---")
    nombre = input("Nombre: ")
    nacionalidad = input("Nacionalidad: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")

    autores = cargar_datos(FILE_AUTHORS)

    nuevo_autor = {

        "nombre": nombre,
        "nacionalidad": nacionalidad,
        "fecha_nacimiento": fecha_nacimiento
    }

    autores.append(nuevo_autor)
    guardar_datos(FILE_AUTHORS, autores)
    print("\n✔️ ¡Autor agregado con éxito!")


def mostrar_informacion():

    print("\n========================================")
    print("      INFORMACIÓN ALMACENADA")
    print("========================================")

    #Cargar datos
    libros = cargar_datos(FILE_BOOKS)
    autores = cargar_datos(FILE_AUTHORS)

    print("\n--- LIBROS ---")
    if not libros:
        print("No hay libros registrados")
    else:
        print(json.dumps(libros, indent=4, ensure_ascii=False))


    print("\n --- AUTORES ---")
    if not autores:
        print("No hay autores registrados")
    else:
        print(json.dumps(autores, indent=4, ensure_ascii=False))
    
    print("============================\n")


def menu():

    #Inicializar archivos si no existen al arrancar

    if not os.path.exists(FILE_BOOKS): guardar_datos(FILE_BOOKS, [])

    if not os.path.exists(FILE_AUTHORS): guardar_datos(FILE_AUTHORS, [])

    while True:

        print("---Sistema de Gestion Bibliografica---")
        print("1. Agregar Libro")
        print("2. Agregar Autor")
        print("3. Mostrar Información")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

 
        if opcion == '1':
            agregar_libro()

        elif opcion == '2':
            agregar_autor()

        elif opcion == '3':
            mostrar_informacion()

        elif opcion == '4':
            print("Saliendo del programa... !Hasta pronto!")
            break

        else:
            print("Opcion no valida. Intente de nuevo.")


if __name__ == "__main__":
    menu()

