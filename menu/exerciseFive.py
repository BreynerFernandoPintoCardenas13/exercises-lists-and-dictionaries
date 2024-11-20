from logic.exerciseFiveList import show_reverse_numbers

def designFiveListMenu():
    while True:
        print("Bienvenido al programa que muestra los números en orden inverso.")
        show_reverse_numbers()
        
        decision = int(input("¿Quieres continuar? Y/1 N/0: "))
        if decision == 0:
            print("¡Hasta luego!")
            break
from logic.exerciseFiveDict import show_subject_credits, input_subject_credits

def designFiveDictMenu():
    while True:
        print("Bienvenido al programa de créditos de asignaturas.")
        
        # Mostrar créditos y permitir al usuario ingresarlos
        show_subject_credits()
        
        # Opción para ingresar los créditos manualmente
        decision = int(input("¿Quieres ingresar los créditos de una asignatura? Y/1 N/0: "))
        if decision == 1:
            input_subject_credits()
        elif decision == 0:
            print("¡Hasta luego!")
            break

