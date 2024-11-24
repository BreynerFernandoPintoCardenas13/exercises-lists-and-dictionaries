import json
def read_file(path):
    with open(f"databases/exerciseFourDict.json", "r") as file:
        data = file.read()
        convertList = json.loads(data)
        return convertList
    
def write_file(data, path):
    with open(f"databases/exerciseFourDict.json", "wb+") as file:
        convertJson = json.dumps(data, indent=4).encode("utf-8")
        file.write(convertJson)
        file.close()
 
def lottery(number):
    data = read_file("exerciseFourList.json")
    data.append(number)
    data.sort()
    write_file(data, "exerciseFourList.json")
    return data

def format_date(date):
    date_parts = date.split("/")
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    data = read_file("exerciseFourDict.json")
    month_ind = int(date_parts[1])
    if not (1 <= month_ind <= 12): 
        raise ValueError("Invalid number for the month, try between 1 - 12")
    format = {
        "day": int(date_parts[0]),
        "month": month[month_ind - 1],
        "year": date_parts[2],
        "message": f"{date_parts[0]} of {month[month_ind - 1]} of {date_parts[2]}"
    }
    data.append(format)
    write_file(data, "exercisesFourDict.json")
    return format.get("message")