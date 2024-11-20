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
            
            case 4:
                from menu.exerciseFour import designFourList
                designFourList()
                


        
