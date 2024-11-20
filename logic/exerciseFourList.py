import json
def read_file(path):
    with open(f"databases/exerciseFourList.json", "r") as file:
        data = file.read()
        convertList = json.loads(data)
        return convertList
    
def write_file(data, path):
    with open(f"databases/exerciseFourList.json", "wb+") as file:
        convertJson = json.dumps(data, indent=4).encode("utf-8")
        file.write(convertJson)
        file.close()
def lottery(number):
    data = read_file("exerciseFourList.json")
    data.append(number)
    data.sort()
    write_file(data, "exerciseFourList.json")
    return data