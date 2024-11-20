from logic.exerciseOneListas import saveCourse
from logic.exerciseOneDict import search_currency
from tabulate import tabulate
def design():
    while True:
        course=input("What is the course name? ")
        rta= saveCourse(course)
        rta= (tabulate(saveCourse(course)))
            
        print(f"\nMaterias: \n{rta}")
        desicion=int(input("You want continue? Y/1 N/0"))
        if desicion==0:
            from main import mainMenu
            mainMenu()
            break
def divisa():
    while True:
        divisas=input("What is currency name? ")
        divisaslower=divisas.lower()
        print(search_currency(divisaslower))
        desicion=int(input("You want continue? Y/1 N/0: "))
        if desicion==0:
            from main import mainMenu
            mainMenu()
            break
        