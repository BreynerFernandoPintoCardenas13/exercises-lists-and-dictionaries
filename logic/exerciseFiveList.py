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

# Función que genera la lista de números, los invierte y los muestra
def show_reverse_numbers():
    # Lista de números del 1 al 10
    numbers = list(range(1, 11))
    
    # Guardar la lista en el archivo JSON
    write_file(numbers, "exerciseFiveList.json")
    
    # Mostrar los números en orden inverso
    print("Los números del 1 al 10 en orden inverso son:")
    print(", ".join(map(str, numbers[::-1])))  # Invertir la lista y mostrarla separada por comas
