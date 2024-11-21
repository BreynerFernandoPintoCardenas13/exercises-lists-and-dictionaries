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

# Función para crear el diccionario de traducción
def create_translation_dict():
    translation_dict = {}
    entries = input("Introduce las traducciones en formato 'palabra:traducción', separadas por comas (ejemplo: 'hola:hello, adiós:goodbye'): ")
    
    # Procesar la entrada para crear el diccionario
    for entry in entries.split(','):
        word, translation = entry.split(':')
        translation_dict[word.strip()] = translation.strip()

    # Guardar el diccionario en el archivo JSON
    write_file(translation_dict, "exerciseOchoDict.json")
    
    return translation_dict

# Función para traducir una frase palabra por palabra
def translate_phrase(phrase, translation_dict):
    translated_phrase = []
    for word in phrase.split():
        translated_word = translation_dict.get(word, word)  # Si la palabra no está en el diccionario, se deja sin traducir
        translated_phrase.append(translated_word)
    
    return " ".join(translated_phrase)

# Función principal para interactuar con el usuario
def dictionary_translation():
    translation_dict = create_translation_dict()
    
    # Pedir una frase en español para traducir
    phrase = input("Introduce la palabra en ingles para traducir: ")
    
    # Traducir la frase
    translated_phrase = translate_phrase(phrase, translation_dict)
    
    print("\nLa traducción es:")
    print(translated_phrase)
