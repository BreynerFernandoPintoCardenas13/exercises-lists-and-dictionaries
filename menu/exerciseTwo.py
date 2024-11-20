from logic.exerciseTwoListas import exerciseTWoList 
from logic.exerciseTwoDict import exerciseTWoDict
from tabulate import tabulate 
def designTwoList():
    while True:
        i=+1
        course=input(f"What is the course name? ")
        rta= (tabulate(exerciseTWoList(course)))
            
        print(f"Yo estudio: \n{rta}")
        desicion=int(input("you want continue? Y/1 N/0"))
        if desicion==0:
            from main import mainMenu
            mainMenu()
            break
def designTwoDic():
    while True:
        i=+1
        data=[]
        name=input(f"What is your name?: ")
        age=int(input("what is your age?:"))
        direction=input("What is your direction?: ")
        telefono=int(input("Which is your phone number?: "))
        print(exerciseTWoDict(data,name, age, direction, telefono))
        
        desicion=int(input("you want continue? Y/1 N/0"))       
        if desicion==0:
            from main import mainMenu
            mainMenu()
            break
    return 0