from logic.exerciseFourList import lottery
from logic.exerciseFour import format_date


def designFourList():
    while True: 
        number = int(input("What is the number? example: 1 ..100 "))
        print(lottery(number))
        desicion=int(input("You want continue? Y/1 N/0"))
        if desicion==0:
            from main import mainMenu
            mainMenu()
            break


def designFourDict():
    while True:
        date = input("What is the date? (05/05/2000)")
        print(format_date(date))
        desicion=int(input("You want continue? Y/1 N/0"))
        if desicion==0:
            from main import mainMenu
            mainMenu()
            break
