import match
def menuDict():
    while True:    
        print(f"""
            EJERCICIOS
        --------------------------
        1. EJERCICIO 1
        2. EJERCICIO 2
        3. EJERCICIO 3
        4. EJERCICIO 4
        5. EJERCICIO 5  
        6. EJERCICIO 6
        7. EJERCICIO 7
    """)
        desicion=int(input("Ingresa una opcion: "))
        match desicion:
            case 1:
                from menu.exerciseOne import divisa
                divisa()
                break
            case 2:
                from menu.exerciseTwo import designTwoDic
                designTwoDic()
                break
            case 3:
                from menu.exerciseTres import designTresDictMenuDict
                designTresDictMenuDict()
            case 4:
                from menu.exerciseFour import designFourDict
                designFourDict()
                break
            case 5:
                from menu.exerciseFive import designFiveDictMenu
                designFiveDictMenu()
            case 6:
                from menu.exerciseSix import designSixMenuDict
                designSixMenuDict()
            case 7:
                from menu.exerciseSeven import designSevenDictMenu
                designSevenDictMenu()
        return 0