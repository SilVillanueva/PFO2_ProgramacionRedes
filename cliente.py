import requests

BASE_URL = 'http://127.0.0.1:5000'  

def registrar_usuario():
    usuario = input("Usuario a registrar: ")
    contraseña = input("Contraseña: ")
    data = {'usuario': usuario, 'contraseña': contraseña}
    response = requests.post(f"{BASE_URL}/registro", json=data)
    print(f"Estado: {response.status_code}")
    print(response.json())

def login_usuario():
    usuario = input("Usuario para login: ")
    contraseña = input("Contraseña: ")
    data = {'usuario': usuario, 'contraseña': contraseña}
    response = requests.post(f"{BASE_URL}/login", json=data)
    print(f"Estado: {response.status_code}")
    print(response.json())

def ver_tareas():
    response = requests.get(f"{BASE_URL}/tareas")
    print(f"Estado: {response.status_code}")
    print("Contenido recibido:")
    print(response.text)

def menu():
    while True:
        print("\n1) Registrar usuario\n2) Login\n3) Ver tareas\n4) Salir")
        opcion = input("Elegí una opción: ")
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            login_usuario()
        elif opcion == '3':
            ver_tareas()
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    menu()
