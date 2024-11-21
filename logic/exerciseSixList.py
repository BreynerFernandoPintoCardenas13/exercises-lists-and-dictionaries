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

# Función para mostrar las asignaturas
def show_subjects():
    subjects = read_file("exerciseSixList.json")
    
    print("\nAsignaturas del curso:")
    for subject in subjects:
        print(subject)

# Función para pedir la nota de cada asignatura
def ask_for_grades():
    subjects = read_file("exerciseSixList.json")
    grades = {}
    
    for subject in subjects:
        while True:
            try:
                grade = float(input(f"Introduce la nota obtenida en {subject}: "))
                if grade < 0 or grade > 10:
                    print("Nota no válida. Debe estar entre 0 y 10. Intenta nuevamente.")
                    continue
                grades[subject] = grade
                break
            except ValueError:
                print("Por favor, ingresa un número válido para la nota.")
    
    # Filtrar las asignaturas aprobadas
    subjects_to_repeat = [subject for subject, grade in grades.items() if grade < 5]
    
    # Guardar las asignaturas que deben repetirse en un archivo
    write_file(subjects_to_repeat, "subjects_to_repeat.json")

# Función para mostrar las asignaturas que deben repetirse
def show_subjects_to_repeat():
    try:
        subjects_to_repeat = read_file("subjects_to_repeat.json")
        if subjects_to_repeat:
            print("\nAsignaturas que debes repetir:")
            for subject in subjects_to_repeat:
                print(subject)
        else:
            print("\n¡Felicidades! No tienes asignaturas para repetir.")
    except FileNotFoundError:
        print("Error al leer las asignaturas a repetir.")
