from logic.exerciseTwoListas import exerciseTWoList
def design2():
    while True:
        i=+1
        course=input(f"What is the course name? ")
        rta= saveCourse(course)
            
        print(f"Yo estudio: {rta}")
        desicion=int(input("you want continue? Y/1 N/2"))
        if desicion==2:
            break