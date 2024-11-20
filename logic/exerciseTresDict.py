import json

# Diccionario con los precios de las frutas
fruit_prices = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

# Función para leer el archivo JSON (aunque no es necesario en este caso, por ahora)
def read_file(path):
    try:
        with open(f"databases/{path}", "r") as file:
            data = file.read()
            return json.loads(data)
    except FileNotFoundError:
        return {}

# Función para escribir los datos al archivo JSON (aunque en este caso no se necesita)
def write_file(data, path):
    with open(f"databases/{path}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Función para preguntar por la fruta y los kilos
def get_fruit_price():
    print("\nFrutas disponibles:", ", ".join(fruit_prices.keys()))
    
    # Pedir la fruta al usuario
    fruit = input("¿Qué fruta quieres comprar? ").capitalize()

    # Comprobar si la fruta está en el diccionario
    if fruit in fruit_prices:
        while True:
            try:
                # Pedir los kilos de la fruta
                kilos = float(input(f"¿Cuántos kilos de {fruit} quieres? "))
                
                if kilos > 0:
                    # Calcular el precio total
                    total_price = kilos * fruit_prices[fruit]
                    print(f"El precio de {kilos} kg(s) de {fruit} es {total_price:.2f}€")
                    break
                else:
                    print("Por favor, ingresa un número de kilos válido mayor que 0.")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número para los kilos.")
    else:
        print(f"La fruta {fruit} no está en el diccionario. Por favor, elige otra.")
