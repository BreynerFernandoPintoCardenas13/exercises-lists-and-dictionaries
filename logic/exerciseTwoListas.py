import json
import tabulate
def read_file():
    with open("exercises-lists-and-dictionaries/databases/exerciseTwoList.json", "r") as file:
        datos = file.read()
        convertirList=json.loads(datos)
        return convertirList

def write_file(datos):
    with open("exercises-lists-and-dictionaries/databases/exerciseTwoList.json", "wb+") as file:
        convertirJson=json.dumps(datos, indent=4).encode("utf-8")
        file.write(convertirJson)
        file.close()
def display_data_in_table(data):
    headers = data[0].keys() if data else []  
    print(tabulate(data, headers=headers, tablefmt="grid"))
        
def exerciseTWoList(course):    
    data=read_file()
    data.append(course)
    write_file(data)
    return data        
