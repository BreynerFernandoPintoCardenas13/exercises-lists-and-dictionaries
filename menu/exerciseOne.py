from logic.exerciseOneListas import saveCourse
from logic.exerciseOneDict import search_currency

def design():
    while True:
        course=input("What is the course name? ")
        rta= saveCourse(course)
        print(rta)  
        desicion=int(input("You want continue? Y/1 N/0"))
        if desicion==0:
            from main import mainMenu
            mainMenu()
            break
def divisa():
    while True:
        divisas=input("What is currency name? ")
        divisas.lower
        print(search_currency(divisas))
        desicion=int(input("You want continue? Y/1 N/0"))
        if desicion==0:
            from main import mainMenu
            mainMenu()
            break
        