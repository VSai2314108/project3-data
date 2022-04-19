import json
import pprint
import requests


base = 'https://vpic.nhtsa.dot.gov/api'

#man_make = requests.get(f'{base}/vehicles/GetMakeForManufacturer/honda?format=json').json()

#mod = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeId/440?format=json').json()

#vin = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/JTDKN3DU7B1398782?format=json&modelyear=2011').json()

#man_det = requests.get(f'{base}/vehicles/GetManufacturerDetails/honda?format=json').json()


if False:
    for r in vin['Results']:
        if r['Value'] is not None and r['Value'] != '' and r['Value'] != 'None':
            pprint(r)


with open("new_mfrs.json") as file:
    mfrs = json.load(file)

with open("new_models.json") as file2:
    models = json.load(file2)

with open("leaders.json") as file3:
    leaders = json.load(file3)

with open("family.json") as file4:
    family = json.load(file4)

with open("new_makes.json") as file5:
    makes = json.load(file5)

with open("types.json") as file6:
    types = json.load(file6)

with open("links.json") as file7:
    links = json.load(file7)

with open("fam_rev.json") as file8:
    fam_rev = json.load(file8)

with open("postal.json") as file9:
    postal = json.load(file9)

data = len(mfrs) + len(models) + len(leaders) + len(family) + len(makes) + len(types) + len(links)
#Matrix Representation
#                 name   Country    State   City   leader   link   makes   types   models
# MfrID            y        y        y        y      y       y      y       n       n
# MfrID
#...
#...[20540]
# MakeID [20540]   y        n         n        n      n       n      n       y       y
# MakeID

#Getting a manufacturer is graph[ID-955]
#Getting a make is graph[20100 + makeID]


count = 0

graph = []
# ADJACENCY MATRIX
for i in range(955, 21495): #21495
    i = str(i)
    if mfrs.get(i) is not None:
        graph.append([mfrs[i]["common"]])
        graph[int(i) - 955].append(mfrs[i]['ctry'])
        graph[int(i) - 955].append(mfrs[i]['state'])
        graph[int(i) - 955].append(mfrs[i]['city'])
        graph[int(i)-955].append([leaders[i]["name"], leaders[i]["pos"]])

        if links.get(i) is not None:
            graph[int(i)-955].append(links[i]["URL"])
        else:
            graph[int(i)-955].append(None)

        if family.get(i) is not None:
            graph[int(i)-955].append(family[i])
        else:
            graph[int(i) - 955].append(None)

    else:
        graph.append(None)

for i in range(20540, 20540 + (11621-440)):
    i = str(i)
    if makes.get(str(int(i)-20100)) is not None:
        graph.append([makes[str(int(i)-20100)]])
        for x in range(6):
            graph[int(i)].append(None)

        if types.get(str(int(i) - 20100)) is not None:
            graph[int(i)].append(types[str(int(i)-20100)])
        else:
            graph[int(i)].append(None)

        if fam_rev.get(str(int(i) - 20100)) is not None:
            graph[int(i)].append(fam_rev[str(int(i)-20100)])
        else:
            graph[int(i)].append(None)
    else:
        graph.append(None)