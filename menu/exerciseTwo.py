from logic.exerciseTwoListas import exerciseTWoList
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
        