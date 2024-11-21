from logic.exerciseNineList import vowel_counter

def designNineListMenu():
    while True:
        print("\nBienvenido al programa para contar las vocales en una palabra.")
        
        # Llamamos a la función para contar las vocales
        vowel_counter()

        # Preguntamos si el usuario desea continuar
        decision = int(input("\n¿Quieres contar las vocales de otra palabra? Y/1 N/0: "))
        if decision == 0:
            print("¡Gracias por usar el programa!")
            break
from logic.exerciseNineDict import add_invoice, pay_invoice, calculate_totals
from logic.exerciseNineDict import read_file, write_file

def designDictMenu():
    # Cargar las facturas desde el archivo JSON (si existen)
    invoices = read_file("exerciseNineDict.json")
    
    while True:
        print("\nBienvenido al sistema de gestión de facturas pendientes.")
        
        # Mostrar las facturas actuales
        print("\nFacturas actuales:")
        for invoice_number, cost in invoices.items():
            print(f"Factura {invoice_number}: {cost} €")
        
        # Mostrar los totales
        calculate_totals(invoices)
        
        # Menú de opciones
        print("\nOpciones:")
        print("1. Añadir una nueva factura")
        print("2. Pagar una factura")
        print("3. Terminar")
        
        # Pedir la opción al usuario
        option = int(input("Selecciona una opción: "))
        
        if option == 1:
            # Añadir una nueva factura
            invoice_number = input("Introduce el número de la factura: ")
            cost = float(input("Introduce el coste de la factura: "))
            invoices = add_invoice(invoice_number, cost, invoices)
            write_file(invoices, "exerciseNineDict.json")
        
        elif option == 2:
            # Pagar una factura
            invoice_number = input("Introduce el número de la factura que deseas pagar: ")
            invoices = pay_invoice(invoice_number, invoices)
            write_file(invoices, "exerciseNineDict.json")
        
        elif option == 3:
            # Terminar
            print("¡Gracias por utilizar el sistema de gestión de facturas!")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

