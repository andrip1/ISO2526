#Fecha: 25/03/2026
#Autor: Andrés Ballester Lozano
import os
import shutil

def leer_archivo():
    archivos = []
    directorios = []

    with open("rutas.txt", "r") as archivo:
        for linea in archivo:
            ruta = linea.strip()
            if os.path.isfile(ruta):
                archivos.append(ruta)
            elif os.path.isdir(ruta):
                directorios.append(ruta)

    return archivos, directorios


def eliminar_fichero():
    nombre_fichero = input("Introduce el nombre del fichero a eliminar: ")
    if os.path.isfile(nombre_fichero):
        try:
            os.remove(nombre_fichero)
            print(f"El fichero {nombre_fichero} ha sido eliminado correctamente.")
        except Exception as e:
            print(f"Error al eliminar el fichero: {e}")
    else:
        print("El fichero no existe.")


def mostrar_informacion_directorio():
    nombre_directorio = input("Introduce el nombre del directorio: ")
    if os.path.isdir(nombre_directorio):
        try:
            print(f"Información del directorio {nombre_directorio}:")
            print(f"Archivos: {os.listdir(nombre_directorio)}")
            print(
                f"Tamaño total: {sum(os.path.getsize(os.path.join(nombre_directorio, f)) for f in os.listdir(nombre_directorio))} bytes")
        except Exception as e:
            print(f"Error al obtener la información: {e}")
    else:
        print("El directorio no existe.")


def copiar_fichero():
    nombre_fichero = input("Introduce el nombre del fichero a copiar: ")
    if os.path.isfile(nombre_fichero):
        destino = input("Introduce el nombre del directorio destino: ")
        if os.path.isdir(destino):
            try:
                shutil.copy(nombre_fichero, destino)
                print(f"Fichero {nombre_fichero} copiado a {destino} correctamente.")
            except Exception as e:
                print(f"Error al copiar el fichero: {e}")
        else:
            print("El directorio destino no existe.")
    else:
        print("El fichero no existe.")


def mostrar_lista(lista):
    if lista:
        print("\nLista de elementos:")
        for item in lista:
            print(item)
    else:
        print("La lista está vacía.")


def main():
    archivos, directorios = leer_archivo()

    while True:
        print("\nElige una opción:")
        print("A - Eliminar un fichero")
        print("B - Mostrar información de un directorio")
        print("C - Copiar un fichero")
        print("D - Mostrar lista elegida")
        print("E - Salir")

        opcion = input("Opción: ").strip().upper()

        if opcion == 'A':
            eliminar_fichero()
        elif opcion == 'B':
            mostrar_informacion_directorio()
        elif opcion == 'C':
            copiar_fichero()
        elif opcion == 'D':
            print("¿Quieres ver la lista de ficheros o directorios?")
            eleccion = input("Escribe 'ficheros' o 'directorios': ").strip().lower()
            if eleccion == 'ficheros':
                mostrar_lista(archivos)
            elif eleccion == 'directorios':
                mostrar_lista(directorios)
            else:
                print("Opción no válida.")
        elif opcion == 'E':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
