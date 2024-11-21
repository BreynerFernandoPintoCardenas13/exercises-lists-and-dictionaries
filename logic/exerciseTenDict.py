import json

# Función para leer el archivo JSON
def read_file(path):
    try:
        with open(f"databases/{path}", "r") as file:
            data = file.read()
            return json.loads(data)
    except FileNotFoundError:
        return {}

# Función para escribir en el archivo JSON
def write_file(data, path):
    with open(f"databases/{path}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Función para añadir un nuevo cliente
def add_client(nif, name, address, phone, email, is_preferential, clients):
    clients[nif] = {
        'name': name,
        'address': address,
        'phone': phone,
        'email': email,
        'preferente': is_preferential
    }
    return clients

# Función para eliminar un cliente por NIF
def delete_client(nif, clients):
    if nif in clients:
        del clients[nif]
    else:
        print(f"No se encontró al cliente con NIF: {nif}")
    return clients

# Función para mostrar la información de un cliente
def show_client(nif, clients):
    if nif in clients:
        client = clients[nif]
        print(f"\nCliente NIF: {nif}")
        print(f"Nombre: {client['name']}")
        print(f"Dirección: {client['address']}")
        print(f"Teléfono: {client['phone']}")
        print(f"Correo: {client['email']}")
        print(f"Preferente: {'Sí' if client['preferente'] else 'No'}")
    else:
        print(f"No se encontró al cliente con NIF: {nif}")

# Función para listar todos los clientes
def list_all_clients(clients):
    if clients:
        for nif, client in clients.items():
            print(f"\nCliente NIF: {nif}")
            print(f"Nombre: {client['name']}")
            print(f"Dirección: {client['address']}")
            print(f"Teléfono: {client['phone']}")
            print(f"Correo: {client['email']}")
            print(f"Preferente: {'Sí' if client['preferente'] else 'No'}")
    else:
        print("No hay clientes registrados.")

# Función para listar solo los clientes preferentes
def list_preferential_clients(clients):
    preferential_clients = {nif: client for nif, client in clients.items() if client['preferente']}
    if preferential_clients:
        for nif, client in preferential_clients.items():
            print(f"\nCliente NIF: {nif}")
            print(f"Nombre: {client['name']}")
            print(f"Dirección: {client['address']}")
            print(f"Teléfono: {client['phone']}")
            print(f"Correo: {client['email']}")
            print(f"Preferente: {'Sí' if client['preferente'] else 'No'}")
    else:
        print("No hay clientes preferentes.")
