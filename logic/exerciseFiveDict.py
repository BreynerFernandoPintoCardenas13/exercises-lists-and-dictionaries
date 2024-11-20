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

# Función que muestra los créditos de cada asignatura y el total de créditos
def show_subject_credits():
    subject_credits = read_file("exerciseFiveDict.json")
    
    # Mostrar los créditos de cada asignatura
    total_credits = 0
    print("\nCréditos de cada asignatura:")
    for subject, credits in subject_credits.items():
        print(f"{subject} tiene {credits} créditos")
        total_credits += credits

    # Mostrar el total de créditos
    print(f"\nEl número total de créditos del curso es: {total_credits}")

# Función para ingresar los créditos de una asignatura
def input_subject_credits():
    subject_credits = read_file("exerciseFiveDict.json")
    
    while True:
        subject = input("Introduce el nombre de la asignatura (o 'salir' para terminar): ").strip()
        
        if subject.lower() == 'salir':
            break
        
        if not subject:
            print("El nombre de la asignatura no puede estar vacío. Intenta nuevamente.")
            continue
        
        try:
            credits = int(input(f"Introduce los créditos para {subject}: "))
            if credits < 0:
                print("Los créditos no pueden ser negativos. Intenta nuevamente.")
                continue
        except ValueError:
            print("Por favor, ingresa un número válido para los créditos.")
            continue
        
        # Añadir o actualizar la asignatura con los créditos ingresados
        subject_credits[subject] = credits
        print(f"Créditos de {subject} actualizados a {credits}.")
    
    # Guardar los créditos en el archivo JSON después de ingresar los datos
    write_file(subject_credits, "exerciseFiveDict.json")
