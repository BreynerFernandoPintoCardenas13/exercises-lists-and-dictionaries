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

# Función para verificar si una palabra es un palíndromo
def is_palindrome(word):
    # Normalizamos la palabra (eliminamos espacios y pasamos a minúsculas)
    cleaned_word = word.replace(" ", "").lower()
    # Comprobamos si la palabra es igual a su reverso
    return cleaned_word == cleaned_word[::-1]

# Función que interactúa con el usuario y muestra si la palabra es un palíndromo
def check_palindrome():
    word = input("Introduce una palabra para verificar si es un palíndromo: ")
    if is_palindrome(word):
        print(f"¡La palabra '{word}' es un palíndromo!")
    else:
        print(f"La palabra '{word}' no es un palíndromo.")
    
    # Guardamos la palabra ingresada en el archivo JSON
    data = read_file("exerciseOChoList.json")
    data.append(word)
    write_file(data, "exerciseOChoList.json")
