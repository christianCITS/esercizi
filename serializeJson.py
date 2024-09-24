import json


def Serialize(dict, file_path) ->bool:
    try:
        with open(file_path,"w") as file_json:
            json.dump(dict,file_json)
            return True
    except Exception as e:
            print("Impossibile eseguire la serializzazione!")
            return False





def Deserialize(file_path) ->dict:
    try:
        with open(file_path,"r") as file:
            return json.load(file)
    except Exception as e:
         print("impossibile eseguire la deserializzazione!")

            


    


a={ "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}
 

fPath="prova.json"

print(Serialize(a,fPath))
print(Deserialize(fPath))


