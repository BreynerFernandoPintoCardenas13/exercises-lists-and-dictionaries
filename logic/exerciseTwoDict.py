import json
import tabulate
def read_file(path):
    with open(f"exercises-lists-and-dictionaries/databases/{path}", "r") as file:
        datos = file.read()
        convertirList=json.loads(datos)
        return convertirList

def write_file(datos, path):
    with open(f"exercises-lists-and-dictionaries/databases/{path}", "wb+") as file:
        convertirJson=json.dumps(datos, indent=4).encode("utf-8")
        file.write(convertirJson)
        file.close()
def display_data_in_table(data):
    headers = data[0].keys() if data else []  
    print(tabulate(data, headers=headers, tablefmt="grid"))
        
def exerciseTWoDict(data, name, age, direction, telefono):    
    data=read_file("exerciseTwoDict.json")
    
    formato={
        "Nombre": name,
        "Edad": age,
        "Direccion": direction,
        "Telefono": telefono
    }
    headers=data[0].keys()
    data.append(formato)
    data=(tabulate(headers=headers, tablefmt="grid"))
    write_file(data, "exerciseTwoDict.json")
    return data        