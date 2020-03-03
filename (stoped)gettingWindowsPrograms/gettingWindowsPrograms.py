
# This not going to work becasue of .exe in installtion location
import winapps
import json


def storingSoftwarelist():
    s = []
    i = 0
    for app in winapps.list_installed():
        data = {}
        i = i+1
        appname = app.name.lower()
        apploc = app.install_location
        data = {
            f'software': [
                f"name: {appname}",
                f"location: {apploc}"
            ]
        }
        s.append(data)
        # print(json
        # .dumps(s))
    return s


def writing():
    data = []
    try:
        with open('data.json', 'r') as f:
            data = json.loads(f.read())
        print(data[0])
    except Exception as identifier:
        print(identifier)
        print("data.json is creating")
        with open('data.json', 'w') as f:
            json.dump(storingSoftwarelist(), f)
            f.close()
def runningRuning(command):
    with open('data.json', 'r') as f:
            data = json.loads(f.read())
    for i in data:
        if "mega" in i["software"][0]:
            print("true")
# writing()
# runningRuning("")