from logic.exerciseFour import lottery, format_date

def designFourList():
    number = int(input("What is the number? example: 1 ..100 "))
    print(lottery(number))
    return 0


def designFourDict():
    date = input("What is the date? (05/05/2000)")
    print(format_date(date))
    desicion=int(input("You want continue? Y/1 N/0"))
    if desicion==1:
        return
    elif desicion==0:
        from menu.mainMenu import menuPrincipal
        menuPrincipal()
