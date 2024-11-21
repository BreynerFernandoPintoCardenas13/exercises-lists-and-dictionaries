import json

# Función para leer el archivo JSON
def read_file(path):
    try:
        with open(f"databases/{path}", "r") as file:
            data = file.read()
            return json.loads(data)
    except FileNotFoundError:
        return []

# Función para escribir en el archivo JSON
def write_file(data, path):
    with open(f"databases/{path}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Función para encontrar el menor y el mayor precio en la lista
def find_min_max(prices):
    min_price = min(prices) if prices else None
    max_price = max(prices) if prices else None
    return min_price, max_price

# Función para mostrar los precios y el menor y mayor precio
def show_prices():
    # Lista de precios predefinidos
    prices = [50, 75, 46, 22, 80, 65, 8]

    # Guardamos la lista de precios en el archivo JSON
    write_file(prices, "exerciseTenList.json")
    
    # Mostrar la lista de precios
    print(f"\nLista de precios: {prices}")
    
    # Encontrar el menor y mayor precio
    min_price, max_price = find_min_max(prices)
    
    # Mostrar los resultados
    print(f"\nEl menor precio es: {min_price}")
    print(f"El mayor precio es: {max_price}")
