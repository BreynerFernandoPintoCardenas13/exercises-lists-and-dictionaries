import json

# Diccionario con los créditos de las asignaturas
subject_credits = {
    "Matemáticas": 6,
    "Física": 4,
    "Química": 5
}

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

# Función que muestra los créditos de cada asignatura y el total de créditos
def show_subject_credits():
    # Guardar el diccionario de asignaturas y créditos en el archivo JSON
    write_file(subject_credits, "exerciseFiveDict.json")
    
    # Mostrar los créditos de cada asignatura
    total_credits = 0
    print("\nCréditos de cada asignatura:")
    for subject, credits in subject_credits.items():
        print(f"{subject} tiene {credits} créditos")
        total_credits += credits

    # Mostrar el total de créditos
    print(f"\nEl número total de créditos del curso es: {total_credits}")
