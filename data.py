import requests
import json
from pprint import pprint

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

#Country Codes -> 0 - 78
#State Codes -> 79 - 1230
#City Codes -> 1231 - 10207
#Leader_Codes -> 10208 - 29207
#Common_Name_Codes -> 29208 - 31257
#Mfr_Codes -> 31258 - 50257
#Make_Codes -> 50258 - 60400
#Model_Codes -> 60401 - 85522
#Link_Codes -> 85523 - 93961
#Type_Codes -> 93961 - 93969
#Postal_Code -> 93970 - 104923

#104,924 total data points

def reverse(to_reverse, file_name):
    rev = {}

    for i in to_reverse:
        rev[to_reverse[i]] = i

    with open(file_name, "w") as nf:
        nf.write(json.dumps(rev, indent=4))

with open("state_codes.json") as sc:
    state_codes = json.load(sc)

with open("state_rev.json") as sr:
    state_rev = json.load(sr)

with open("ctry_codes.json") as cc:
    ctry_codes = json.load(cc)

with open("ctry_rev.json") as cr:
    ctry_rev = json.load(cr)

with open("mfr_codes.json") as mc:
    mfr_codes = json.load(mc)

with open("mfr_rev.json") as mr:
    mfr_rev = json.load(mr)

with open("city_codes.json") as yc:
    city_codes = json.load(yc)

with open("city_rev.json") as yr:
    city_rev = json.load(yr)

with open("leader_codes.json") as lc:
    leader_codes = json.load(lc)

with open("leader_rev.json") as lr:
    leader_rev = json.load(lr)

with open("postal_codes.json") as pc:
    postal_codes = json.load(pc)

with open("postal_code_rev.json") as pr:
    postal_rev = json.load(pr)

with open("common_codes.json") as oc:
    common_codes = json.load(oc)

with open("common_rev.json") as o_r:
    common_rev = json.load(o_r)

with open("link_codes.json") as ic:
    link_codes = json.load(ic)

with open("link_rev.json") as ir:
    link_rev = json.load(ir)

with open("make_codes.json") as ac:
    make_codes = json.load(ac)

with open("make_rev.json") as ar:
    make_rev = json.load(ar)

with open("model_codes.json") as dc:
    model_codes = json.load(dc)

with open("model_rev.json") as dr:
    model_rev = json.load(dr)

with open("type_codes.json") as tc:
    type_codes = json.load(tc)

with open("type_rev.json") as tr:
    type_rev = json.load(tr)


if True:
    adj_list = []

    for i in range(104924):
        adj = set()
        adj_list.append(adj)

    #Set ctry, state, city adjacencies
    for m in mfrs:

        ctry = mfrs[m]['ctry']
        if ctry == '':
            ccode = None
        else:
            ccode = int(ctry_rev[ctry])

        state = mfrs[m]['state']
        if state is None:
            scode = None
        else:
            scode = int(state_rev[state])

        city = mfrs[m]['city']
        if city is None:
            ycode = None
        else:
            ycode = int(city_rev[city])

        pos = postal[m]['postal']
        if pos is None:
            pcode = None
        else:
            pcode = int(postal_rev[pos])

        leader = leaders[m]['name']
        if leader is None:
            lcode = None
        else:
            lcode = int(leader_rev[m])

        common = mfrs[m]['common']
        if common is None:
            ocode = None
        else:
            ocode = int(common_rev[common])

        if links.get(m) is not None:
            icode = int(link_rev[m])
        else:
            icode = None

        if family.get(m) is not None:
            mks = family[m]
            mcodes = []
            for mk in mks:
                mcodes.append(int(make_rev[str(mk)]))
        else:
            mcodes = None



        if ccode is not None and scode is not None:
            adj_list[ccode].add(scode)
            adj_list[int(mfr_rev[m])].add(ccode)
            adj_list[int(mfr_rev[m])].add(scode)
        elif ccode is not None:
            adj_list[int(mfr_rev[m])].add(ccode)
        elif scode is not None:
            adj_list[int(mfr_rev[m])].add(scode)

        if scode is not None and ycode is not None:
            adj_list[scode].add(ycode)
            adj_list[int(mfr_rev[m])].add(ycode)
        elif ycode is not None:
            adj_list[int(mfr_rev[m])].add(ycode)

        if ccode is not None and pcode is not None:
            adj_list[ccode].add(pcode)
            adj_list[int(mfr_rev[m])].add(pcode)
        elif pcode is not None:
            adj_list[int(mfr_rev[m])].add(pcode)

        if pcode is not None and lcode is not None:
            adj_list[pcode].add(lcode)
            adj_list[int(mfr_rev[m])].add(lcode)
        elif lcode is not None:
            adj_list[int(mfr_rev[m])].add(lcode)

        if lcode is not None and ocode is not None:
            adj_list[lcode].add(ocode)
            adj_list[int(mfr_rev[m])].add(ocode)
        elif ocode is not None:
            adj_list[int(mfr_rev[m])].add(ocode)
            adj_list[ocode].add(int(mfr_rev[m]))

        if icode is not None:
            adj_list[int(mfr_rev[m])].add(icode)

        if mcodes is not None:
            for code in mcodes:
                adj_list[code].add(int(mfr_rev[m]))
                adj_list[int(mfr_rev[m])].add(code)

                make_id = make_codes[str(code)]

                if fam_rev.get(make_id) is not None:
                    for model in fam_rev[make_id]:
                        adj_list[code].add(int(model_rev[model]))
                        adj_list[int(model_rev[model])].add(code)

                if types.get(make_id) is not None:
                    for typ in types[make_id]:
                        adj_list[code].add(int(type_rev[str(typ['type_id'])]))
                        adj_list[int(type_rev[str(typ['type_id'])])].add(code)


    if False:
        count = 0
        for i in range(len(adj_list)):
            if len(adj_list[i]) == 0:
                continue
            else:
                print(f"{i}: {adj_list[i]}")
                count += len(adj_list[i])

    edge_list = []

    for row in range(len(adj_list)):
        for col in adj_list[row]:
            edge_list.append([row, col])


adj_list_dict = {}

for i in range(len(adj_list)):

    s = adj_list[i]
    row = []
    
    for x in s:
        row.append(x)

    adj_list_dict[i] = row


edge_list_dict = {}

for i in range(len(edge_list)):
    edge_list_dict[i] = edge_list[i]

with open("adj_list.json", "w") as al:
    al.write(json.dumps(adj_list_dict, indent=4))

with open("edge_list.json", "w") as al:
    al.write(json.dumps(edge_list_dict, indent=4))


