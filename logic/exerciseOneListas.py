import json
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
        
def saveCourse(course):    
    data=read_file("exercisesOneListas.json")
    data.append(course)
    write_file(data, "exercisesOneListas.json")
    return data        
