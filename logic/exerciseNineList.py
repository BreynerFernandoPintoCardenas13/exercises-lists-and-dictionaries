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

# Función para contar las vocales en una palabra
def count_vowels(word):
    vowels = "aeiou"
    vowel_count = {v: 0 for v in vowels}  # Diccionario para contar las vocales
    
    for letter in word.lower():
        if letter in vowels:
            vowel_count[letter] += 1
    
    return vowel_count

# Función principal que muestra el número de veces que aparece cada vocal
def vowel_counter():
    word = input("Introduce una palabra para contar las vocales: ")
    
    # Contar las vocales en la palabra
    vowel_count = count_vowels(word)
    
    # Mostrar los resultados
    print(f"\nNúmero de veces que aparece cada vocal en la palabra '{word}':")
    for vowel, count in vowel_count.items():
        print(f"{vowel.upper()}: {count}")
    
    # Guardamos la palabra y el conteo de las vocales en el archivo JSON
    data = read_file("exerciseNineList.json")
    data.append({"word": word, "vowel_count": vowel_count})
    write_file(data, "exerciseNineList.json")
