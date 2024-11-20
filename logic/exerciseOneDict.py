import json
def read_file(path):
    with open(f"databases/{path}", "r") as file:
        datos = file.read()
        convertirList=json.loads(datos)
        return convertirList

def write_file(datos, path):
    with open(f"databases/{path}", "wb+") as file:
        convertirJson=json.dumps(datos, indent=4).encode("utf-8")
        file.write(convertirJson)
        file.close()
               

def search_currency(currency):
    data = read_file("exerciseOneDict.json")
    if (data.get(currency)):
        return data.get(currency)
    else:
        return "Currency not found"