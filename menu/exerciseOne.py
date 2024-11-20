from logic.exerciseOneListas import saveCourse

def design():
    while True:
        course=input("What is the course name? ")
        rta= saveCourse(course)
        
        print(rta)  
        desicion=int(input("You want continue? Y/1 N/0"))
        if desicion==0:
            break