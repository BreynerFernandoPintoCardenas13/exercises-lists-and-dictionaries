import json
def read_file():
    with open("databases/exerciseTWoList.json", "r") as file:
        datos = file.read()
        convertirList=json.loads(datos)
        return convertirList

def write_file(datos):
    with open("databases/exerciseTWoList.json", "wb+") as file:
        convertirJson=json.dumps(datos, indent=4).encode("utf-8")
        file.write(convertirJson)
        file.close()
        
def exerciseTWoList(course):    
    data=read_file()
    data.append(course)
    write_file(data)
    return data        
