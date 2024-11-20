import match
def menuListas():
    while True:    
        print(f"""
            EJERCICIOS
        --------------------------
        1. EJERCICIO 1
        4. EJERCICIOS 4   
    """)
        desicion=int(input("Ingresa una opcion"))
        match desicion:
            case 1:
                from menu.exerciseOne import design
                design()
                return design()
                break
            
            case 4:
                from menu.exerciseFour import designFourList
                return designFourList()
                break
        return 0

        
