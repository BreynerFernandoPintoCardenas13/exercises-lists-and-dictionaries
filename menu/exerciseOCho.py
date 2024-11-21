from logic.exerciseOChoList import check_palindrome

def designOchoListMenu():
    while True:
        print("\nBienvenido al programa que verifica si una palabra es un palíndromo.")
        
        # Llamamos a la función que verifica si la palabra es un palíndromo
        check_palindrome()

        # Preguntamos si el usuario desea continuar
        decision = int(input("\n¿Quieres comprobar otra palabra? Y/1 N/0: "))
        if decision == 0:
            print("¡Gracias por usar el programa!")
            break
from logic.exerciseOchoDict import dictionary_translation

def designOchoDictMenu():
    while True:
        print("\nBienvenido al programa de traducción español-inglés.")
        
        # Llamamos a la función principal de traducción
        dictionary_translation()

        # Preguntamos si el usuario desea continuar
        decision = int(input("\n¿Quieres realizar otra traducción? Y/1 N/0: "))
        if decision == 0:
            print("¡Gracias por usar el programa!")
            break
