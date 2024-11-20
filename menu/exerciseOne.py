from logic.exerciseOneListas import saveCourse
from logic.exerciseOneDict import search_currency

def design():
    while True:
        course=input("What is the course name? ")
        rta= saveCourse(course)
        print(rta)  
        desicion=int(input("You want continue? Y/1 N/0"))
        if desicion==1:
            return
        elif desicion==0:
            from menu.mainMenu import menuPrincipal
            menuPrincipal()
def divisa():
    divisas=input("What is currency name? ")
    divisas.lower
    print(search_currency(divisas))