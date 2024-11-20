import match
def menuListas():
    while True:    
        print(f"""
            EJERCICIOS
        --------------------------
        1. EJERCICIO 1
        2. EJERCICIO 2
        3. EJERCICIO 3
        4. EJERCICIO 4   
        5. EJERCICIO 5
    """)
        desicion=int(input("Ingresa una opcion: "))
        match desicion:
            case 1:
                from menu.exerciseOne import design
                design()
            case 2:
                from menu.exerciseTwo import designTwoList
                designTwoList()
            case 3:
                from menu.exerciseTres import designTresMenu
                designTresMenu()
            case 4:
                from menu.exerciseFour import designFourList
                designFourList()
            case 5:
                from menu.exerciseFive import designFiveListMenu
                designFiveListMenu()
            
                


        
