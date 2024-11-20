import match
def menuListas():
    print(f"""
        TIPO DE EJERCICIOS
    --------------------------
    1. EJERCICIO 1
    2. EJERCICIOS 4   
""")
    desicion=int(input("Ingresa una opcion"))
    match desicion:
        case 1:
            from menu.exerciseOne import design
            design()
            return design()
        
        case 4:
            from menu.exerciseFour import designFourList
            return designFourList()
    return 0

    
