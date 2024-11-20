import match
def menuDict():
    while True:    
        print(f"""
            EJERCICIOS
        --------------------------
        1. EJERCICIO 1
        2. EJERCICIO 2
        4. EJERCICIOS 4   
    """)
        desicion=int(input("Ingresa una opcion"))
        match desicion:
            case 1:
                from menu.exerciseOne import divisa
                divisa()
                break
            case 2:
                from menu.exerciseTwo import designTwoDic
                designTwoDic()
                break
            case 4:
                from menu.exerciseFour import designFourDict
                designFourDict()
                break
        return 0