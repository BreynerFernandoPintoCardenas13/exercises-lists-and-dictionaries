import json
def read_file():
    with open("databases/exercisesOneListas.json", "r") as file:
        datos = file.read()
        convertirList=json.loads(datos)
        return convertirList

def write_file(datos):
    with open("databases/exercisesOneListas.json", "wb+") as file:
        convertirJson=json.dumps(datos, indent=4).encode("utf-8")
        file.write(convertirJson)
        file.close()
        
def saveCourse(course):    
    data=read_file()
    data.append(course)
    write_file(data)
    return data        
