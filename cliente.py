import requests

BASE_URL = 'http://127.0.0.1:5000'

def registrar():
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    res = requests.post(f'{BASE_URL}/registro', data={
        'usuario': usuario,
        'contraseña': contraseña
    })

    print("→ Respuesta:", res.text)

def login():
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    session = requests.Session()
    res = session.post(f'{BASE_URL}/login', data={
        'usuario': usuario,
        'contraseña': contraseña
    })

    print("→ Respuesta login:", res.text)

    if "Sesión iniciada correctamente." in res.text:
        tareas = session.get(f'{BASE_URL}/tareas')
        print("→ Contenido de /tareas:")
        print(tareas.text)
    else:
        print("Login fallido.")

def menu():
    while True:
        print("\n=== Cliente de Consola ===")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == '1':
            registrar()
        elif opcion == '2':
            login()
        elif opcion == '3':
            break
        else:
            print("Opción inválida")

if __name__ == '__main__':
    menu()
