from logic.exerciseTenList import show_prices

def designTenMenu():
    while True:
        print("\nBienvenido al programa de precios.")
        
        # Mostrar los precios y el menor y mayor precio
        show_prices()
        
        # Preguntar si desea continuar
        decision = int(input("\n¿Quieres ver los precios nuevamente? Y/1 N/0: "))
        if decision == 0:
            print("¡Hasta luego!")
            break
from logic.exerciseTenDict import add_client, delete_client, show_client, list_all_clients, list_preferential_clients
from logic.exerciseTenDict import read_file, write_file

def designDictMenu():
    # Cargar los clientes desde el archivo JSON
    clients = read_file("exerciseTenDict.json")
    
    while True:
        print("\nMenú de Gestión de Clientes:")
        print("1. Añadir cliente")
        print("2. Eliminar cliente")
        print("3. Mostrar cliente")
        print("4. Listar todos los clientes")
        print("5. Listar clientes preferentes")
        print("6. Terminar")
        
        # Pedir la opción al usuario
        option = int(input("Selecciona una opción: "))
        
        if option == 1:
            # Añadir un nuevo cliente
            nif = input("Introduce el NIF del cliente: ")
            name = input("Introduce el nombre del cliente: ")
            address = input("Introduce la dirección del cliente: ")
            phone = input("Introduce el teléfono del cliente: ")
            email = input("Introduce el correo electrónico del cliente: ")
            is_preferential = input("¿Es un cliente preferente? (s/n): ").lower() == 's'
            clients = add_client(nif, name, address, phone, email, is_preferential, clients)
            write_file(clients, "exerciseTenDict.json")
        
        elif option == 2:
            # Eliminar un cliente
            nif = input("Introduce el NIF del cliente a eliminar: ")
            clients = delete_client(nif, clients)
            write_file(clients, "exerciseTenDict.json")
        
        elif option == 3:
            # Mostrar un cliente
            nif = input("Introduce el NIF del cliente a mostrar: ")
            show_client(nif, clients)
        
        elif option == 4:
            # Listar todos los clientes
            list_all_clients(clients)
        
        elif option == 5:
            # Listar clientes preferentes
            list_preferential_clients(clients)
        
        elif option == 6:
            # Terminar
            print("¡Gracias por utilizar el sistema de gestión de clientes!")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
