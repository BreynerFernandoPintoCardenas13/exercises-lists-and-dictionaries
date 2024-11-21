from logic.exerciseSixList import show_subjects, ask_for_grades, show_subjects_to_repeat

def designSixMenu():
    while True:
        print("Bienvenido al programa de gestión de asignaturas y notas.")
        
        # Mostrar las asignaturas y permitir al usuario ingresar las notas
        show_subjects()
        
        ask_for_grades()
        
        # Mostrar las asignaturas que deben repetirse
        show_subjects_to_repeat()
        
        # Preguntar si el usuario quiere continuar o salir
        decision = int(input("¿Quieres continuar? Y/1 N/0: "))
        if decision == 0:
            print("¡Hasta luego!")
            break
from logic.exerciseSixDict import add_data_to_dict

def designSixMenuDict():
    user_data = {}  # Diccionario vacío para almacenar la información

    while True:
        print("\nBienvenido al programa para crear un perfil personal.")
        
        # Llamar a la función para agregar datos al diccionario
        add_data_to_dict(user_data)
        
        # Preguntar si el usuario quiere continuar o salir
        decision = int(input("¿Quieres agregar otro dato? Y/1 N/0: "))
        if decision == 0:
            print("¡Hasta luego!")
            break

