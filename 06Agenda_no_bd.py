import os

# Lista para almacenar los contactos
agenda = []

# Función para agregar un contacto


def agregar_contacto(nombre, telefono, email):
    contacto = {'nombre': nombre, 'telefono': telefono, 'email': email}
    agenda.append(contacto)
    print(f"Contacto {nombre} agregado.")

# Función para ver todos los contactos


def ver_contactos():
    if not agenda:
        print("No hay contactos en la agenda.")
    else:
        for i, contacto in enumerate(agenda):
            print(f"Contacto {i + 1}:")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Teléfono: {contacto['telefono']}")
            print(f"Email: {contacto['email']}")
            print("-" * 20)

# Función para buscar un contacto por nombre


def buscar_contacto(nombre):
    for contacto in agenda:
        if contacto['nombre'].lower() == nombre.lower():
            print("Contacto encontrado:")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Teléfono: {contacto['telefono']}")
            print(f"Email: {contacto['email']}")
            return
    print("Contacto no encontrado.")

# Función para eliminar un contacto por nombre


def eliminar_contacto(nombre):
    for i, contacto in enumerate(agenda):
        if contacto['nombre'].lower() == nombre.lower():
            del agenda[i]
            print(f"Contacto {nombre} eliminado.")
            return
    print("Contacto no encontrado.")

# Menú de opciones


def menu():
    os.system('cls')
    while True:
        print("\nAgenda de Contactos")
        print("1. Agregar Contacto")
        print("2. Ver Contactos")
        print("3. Buscar Contacto")
        print("4. Eliminar Contacto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            email = input("Ingrese el email: ")
            agregar_contacto(nombre, telefono, email)
        elif opcion == '2':
            ver_contactos()
        elif opcion == '3':
            nombre = input("Ingrese el nombre a buscar: ")
            buscar_contacto(nombre)
        elif opcion == '4':
            nombre = input("Ingrese el nombre a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == '5':
            print("Saliendo de la agenda de contactos.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecución del menú
menu()
