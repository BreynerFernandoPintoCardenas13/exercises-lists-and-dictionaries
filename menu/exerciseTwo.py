from logic.exerciseTwoListas import exerciseTWoList 
from logic.exerciseTwoDict import exerciseTWoDict 
def designTwoList():
    while True:
        i=+1
        course=input(f"What is the course name? ")
        rta= exerciseTWoList(course)
            
        print(f"Yo estudio: {rta}")
        desicion=int(input("you want continue? Y/1 N/0"))
        if desicion==0:
            from main import mainMenu
            mainMenu()
            break
def designTwoDic():
    while True:
        i=+1
        name=input(f"What is your name?: ")
        age=int(input("what is your age?:"))
        direction=input("What is your direction?: ")
        telefono=int(input("Which is your phone number?: "))
        print(exerciseTWoDict(name, age, direction, telefono))
        
        desicion=int(input("you want continue? Y/1 N/0"))       
        if desicion==0:
            from main import mainMenu
            mainMenu()
            break
    return 0