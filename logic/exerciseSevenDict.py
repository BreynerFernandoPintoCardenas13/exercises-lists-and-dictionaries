import json

# Función para leer el archivo JSON (por si deseas almacenar los artículos)
def read_file(path):
    try:
        with open(f"databases/{path}", "r") as file:
            data = file.read()
            return json.loads(data)
    except FileNotFoundError:
        return {}

# Función para escribir en el archivo JSON (para guardar la cesta de la compra)
def write_file(data, path):
    with open(f"databases/{path}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Función para gestionar la cesta de la compra
def manage_shopping_cart():
    shopping_cart = {}

    while True:
        item = input("Introduce el nombre del artículo (o escribe 'terminar' para finalizar): ")
        
        if item.lower() == 'terminar':
            break
        
        try:
            price = float(input(f"Introduce el precio de {item}: "))
        except ValueError:
            print("Por favor, introduce un precio válido.")
            continue
        
        shopping_cart[item] = price
    
    # Guardar los artículos en el archivo JSON
    write_file(shopping_cart, "exerciseSevenDict.json")

    return shopping_cart
