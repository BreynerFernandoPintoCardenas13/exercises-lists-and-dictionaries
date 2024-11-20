import json

# Lista de asignaturas
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Función para leer el archivo JSON
def read_file(path):
    try:
        with open(f"databases/{path}", "r") as file:
            data = file.read()
            return json.loads(data)
    except FileNotFoundError:
        return {}

# Función para escribir los datos al archivo JSON
def write_file(data, path):
    with open(f"databases/{path}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Función para pedir y guardar las notas
def get_notes():
    # Inicializa un diccionario para almacenar las notas
    notes = {}

    # Recorre las asignaturas y pide la nota para cada una
    for subject in subjects:
        while True:
            try:
                note = float(input(f"¿Qué nota has sacado en {subject}? "))
                if 0 <= note <= 10:
                    notes[subject] = note
                    break
                else:
                    print("Nota inválida, por favor ingresa una nota entre 0 y 10.")
            except ValueError:
                print("Entrada no válida. Por favor ingresa un número.")

    # Muestra las notas de las asignaturas
    print("\nResumen de las notas:")
    for subject, note in notes.items():
        print(f"En {subject} has sacado {note}")

    # Guardar las notas en un archivo JSON
    write_file(notes, "exerciseTresList.json")