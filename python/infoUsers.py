#Autor: Andrés Ballester Lozano
#Fecha: 25/03/2026
import os
import platform
import pwd
import subprocess
import sys
import cpuinfo

def check_root():
    if os.geteuid() != 0:
        print("Este script debe ejecutarse como root.")
        sys.exit(1)

def system_info():
    print("\n--- Información del Sistema ---")
    print(f"Sistema operativo: {platform.system()} {platform.release()}")
    print(f"Versión: {platform.version()}")
    print(f"Arquitectura: {platform.machine()}")

    print("\n--- Información de la CPU ---")
    print(f"Procesador: {platform.processor()}")
    print(f"Núcleos: {os.cpu_count()}")
    print(f"Nombre: {os.cpuinfo()}")

def user_info():
    username = input("Introduce el nombre de usuario: ")

    try:
        user = pwd.getpwnam(username)
        print("\nEl usuario existe. Información:")
        print(f"UID: {user.pw_uid}")
        print(f"GID: {user.pw_gid}")
        print(f"Directorio home: {user.pw_dir}")
        print(f"Shell: {user.pw_shell}")
    except KeyError:
        print("\nEl usuario no existe. Creándolo...")
        try:
            subprocess.run(["useradd", username], check=True)
            print(f"Usuario '{username}' creado correctamente.")
        except subprocess.CalledProcessError:
            print("Error al crear el usuario.")

def directory_check():
    path = input("Introduce la ruta del directorio: ")

    if os.path.exists(path):
        if os.path.isdir(path):
            print("El directorio existe.")
        else:
            print("Existe pero no es un directorio.")
    else:
        try:
            os.makedirs(path)
            print("Directorio creado correctamente.")
        except Exception as e:
            print(f"Error al crear el directorio: {e}")

def menu():
    while True:
        print("\n===== MENÚ =====")
        print("1. Información del sistema y CPU")
        print("2. Comprobar/crear usuario")
        print("3. Comprobar/crear directorio")
        print("4. Salir")

        option = input("Selecciona una opción: ")

        if option == "1":
            system_info()
        elif option == "2":
            user_info()
        elif option == "3":
            directory_check()
        elif option == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    check_root()
    menu()
