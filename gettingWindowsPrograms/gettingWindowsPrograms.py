import winapps
import json


def storingSoftwarelist():
    s=[]
    i=0
    for app in winapps.list_installed():
        data={}
        i=i+1
        appname=app.name
        apploc=app.install_location
        data={
            f'software':[
                f"name: {appname}",
                f"location: {apploc}"
            ]
        }
        s.append(data)
        # print(json
        # .dumps(s))
    return s    


# with open('data.json', 'w') as f:
    # json.dump(storingSoftwarelist(), f)

with open('data.json', 'r') as f:
    json_text = f.reads()

# Decode the JSON string into a Python dictionary.
data = json.loads(f'{json_text}')

for key, value in data.items():    
    print (key)