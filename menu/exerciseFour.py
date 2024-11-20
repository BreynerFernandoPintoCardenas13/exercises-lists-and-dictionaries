from logic.exerciseFour import lottery, format_date

def designFourList():
    number = int(input("What is the number? example: 1 ..100 "))
    print(lottery(number))
    return 0


def designFourDict():
    date = input("What is the date? ")
    print(format_date(date))
    return 0