import app
import os
import json

def __init__path():
    with open("app/schema.json", "r") as file:
        data = json.load(file)
    file.close()
    
    data["path"] = os.path.dirname(os.path.abspath(__file__))
    
    with open("app/schema.json", "w") as file:
        json.dump(data, file, indent=4) 
    
    file.close()# indent for pretty formatting

if __name__ == "__main__":
    __init__path()
    app.main()
