from logic.exerciseTresLists import get_notes

def designTresMenu():
    while True:
        print("Bienvenido al sistema de notas.")
        get_notes()
        
        desicion = int(input("¿Quieres continuar? Y/1 N/0: "))
        if desicion == 0:
            print("¡Hasta luego!")
            break
from logic.exerciseTresDict import get_fruit_price

def designTresDictMenuDict():
    while True:
        print("Bienvenido al sistema de precios de frutas.")
        get_fruit_price()
        
        decision = int(input("¿Quieres continuar? Y/1 N/0: "))
        if decision == 0:
            print("¡Hasta luego!")
            break
