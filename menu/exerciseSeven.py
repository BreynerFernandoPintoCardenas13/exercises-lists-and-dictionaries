from logic.exerciseSevenList import modify_alphabet

def designSevenMenu():
    while True:
        print("\nBienvenido al programa de modificación del abecedario.")
        
        # Llamar a la función que modifica el abecedario
        modified_alphabet = modify_alphabet()
        
        # Mostrar el resultado
        print("\nEl abecedario modificado es:")
        print(modified_alphabet)
        
        decision = int(input("¿Quieres continuar? Y/1 N/0: "))
        if decision == 0:
            print("¡Hasta luego!")
            break
from tabulate import tabulate
from logic.exerciseSevenDict import manage_shopping_cart

def designSevenDictMenu():
    while True:
        print("\nBienvenido al programa para gestionar tu cesta de la compra.")
        
        # Llamar a la función que gestiona la cesta de la compra
        shopping_cart = manage_shopping_cart()

        # Mostrar la lista de la compra
        print("\n| Lista de la compra     |        |")
        print("| :--------------------  | -----: |")
        total_cost = 0
        items = []
        for item, price in shopping_cart.items():
            items.append([item, f"{price:.2f}€"])
            total_cost += price
        
        # Mostrar artículos
        print(tabulate(items, tablefmt="plain"))
        
        # Mostrar el total
        print(f"| Total                 | {total_cost:.2f}€ |")

        decision = int(input("\n¿Quieres continuar añadiendo artículos? Y/1 N/0: "))
        if decision == 0:
            print("¡Gracias por usar el programa!")
            break
