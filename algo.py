import json
from pprint import pprint
import requests

vin = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/JTDKN3DU7B1398782?format=json&modelyear=2011').json()

vin_det = {}

for r in vin['Results']:
    if r['Value'] is not None and r['Value'] != '' and r['Value'] != 'None':
        vin_det[r['Variable']] = {'id': r['VariableId'], 'value': r['Value']}

with open("adj_list.json") as file:
    adj_dict = json.load(file)

with open("edge_list.json") as file2:
    edge_dict = json.load(file2)

adj_list = []
for i in range(len(adj_dict)):
    adj_list.append(adj_dict[str(i)])

edge_list = []
for i in range(len(edge_dict)):
    edge_list.append(edge_dict[str(i)])
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

with open("code_master.json") as file3:
    master_codes = json.load(file3)

with open("mfr_by_name.json") as nf:
    mfr_name = json.load(nf)

with open("makes_by_name.json") as nf:
    make_name = json.load(nf)

with open("type_name.json") as nf:
    type_name = json.load(nf)

with open("new_mfrs.json") as file:
    mfrs = json.load(file)

with open("leaders.json") as file3:
    leaders = json.load(file3)

with open("links.json") as file7:
    links = json.load(file7)

with open("new_makes.json") as file5:
    makes = json.load(file5)

with open("new_models.json") as file2:
    models = json.load(file2)

def get_mfrs_in_country(ctry):
    if ctry_rev.get(ctry) is not None:
        ctry_code = int(ctry_rev[ctry])
        nodes = adj_list[ctry_code]


        mfrs = set()
        states = []

        for n in nodes:
            states.append(n)

        for state in states:
            for city in adj_list[state]:
                for postal in adj_list[city]:
                    for leader in adj_list[postal]:
                        for common in adj_list[leader]:
                            for mfr in adj_list[common]:
                                mfrs.add(mfr)
        return mfrs
    else:
        return None

def get_mfrs_in_state(state):
    if state_rev.get(state) is not None:
        state_code = int(state_rev[state])
        nodes = adj_list[state_code]

        mfrs = set()
        cities = []

        for n in nodes:
            if 1231 <= n <= 10207:
                cities.append(n)

        for city in cities:
            for postal in adj_list[city]:
                for leader in adj_list[postal]:
                    for common in adj_list[leader]:
                        for mfr in adj_list[common]:
                            mfrs.add(mfr)
        return mfrs
    else:
        return None

def get_mfrs_in_city(city):
    if city_rev.get(city) is not None:
        city_code = int(city_rev[city])
        nodes = adj_list[city_code]

        mfrs = set()
        postals = []

        for n in nodes:
            if 93970 <= n <= 104923:
                postals.append(n)

            for postal in postals:
                for leader in adj_list[postal]:
                    for common in adj_list[leader]:
                        for mfr in adj_list[common]:
                            mfrs.add(mfr)
        return mfrs
    else:
        return None

def get_makes_by_mfr(mfr):
    mfr = mfr_name[mfr]
    if mfr_rev.get(mfr) is not None:
        mfr_code = int(mfr_rev[mfr])
        nodes = adj_list[mfr_code]

        makes = set()

        for n in nodes:
            if 50258 <= n <= 60400:
                makes.add(n)

        return makes
    else:
        return None

def get_models_by_make(make):
    make = make_name[make]
    if make_rev.get(make) is not None:
        make_code = int(make_rev[make])
        nodes = adj_list[make_code]

        models = set()

        for n in nodes:
            if 60401 <= n <= 85522:
                models.add(n)

        return models
    else:
        return None

def get_makes_by_type(type):
    type = str(type_name[type])
    if type_rev.get(type) is not None:
        type_code = int(type_rev[type])
        nodes = adj_list[type_code]

        makes = set()

        for n in nodes:
            if 50258 <= n <= 60400:
                makes.add(n)

        return makes
    else:
        return None

def get_postal_by_mfr(mfr):
    mfr = mfr_name[mfr]
    if mfr_rev.get(mfr) is not None:
        mfr_code = int(mfr_rev[mfr])
        nodes = adj_list[mfr_code]

        postals = set()

        for n in nodes:
            if 93970 <= n <= 104923:
                postals.add(n)

        return postals
    else:
        return None

def get_mfrs_by_postal(postal):
    if postal_rev.get(postal) is not None:
        postal_code = int(postal_rev[postal])
        nodes = adj_list[postal_code]

        mfrs = set()

        for n in nodes:
            if 31258 <= n <= 50257:
                mfrs.add(n)

        return mfrs
    else:
        return None

def get_leader_by_mfr(mfr):
    mfr = mfr_name[mfr]
    if mfr_rev.get(mfr) is not None:
        mfr_code = int(mfr_rev[mfr])
        nodes = adj_list[mfr_code]

        leader = 0

        for n in nodes:
            if 10208 <= n <= 29207:
                leader = n

        if leader == 0:
            return None
        return leader
    else:
        return None

def get_mfrs_by_leader(leader):
    if leader_rev.get(leader) is not None:
        leader_code = int(leader_rev[leader])
        nodes = adj_list[leader_code]

        common = set()

        for n in nodes:
            if 29208 <= n <= 31257:
                common.add(n)

        mfrs = set()

        for c in common:
            mfs = adj_list[c]
            for m in mfs:
                mfrs.add(m)

        return mfrs
    else:
        return None

def get_link_by_mfr(mfr):
    mfr = mfr_name[mfr]
    if mfr_rev.get(mfr) is not None:
        mfr_code = int(mfr_rev[mfr])
        nodes = adj_list[mfr_code]

        link = 0

        for n in nodes:
            if 85523 <= n <= 93961:
                link = n

        if link == 0:
            return None
        return link
    else:
        return None

def get_mfrs_with_same_common_as_(mfr):
    mfr = mfr_name[mfr]
    if mfr_rev.get(mfr) is not None:
        mfr_code = int(mfr_rev[mfr])
        nodes = adj_list[mfr_code]

        commons = set()

        for n in nodes:
            if 29208 <= n <= 31257:
                commons.add(n)

        ms = []
        for c in commons:
            for m in adj_list[c]:
                print(m)
                ms.append(mfrs[mfr_codes[str(m)]]['name'])

        return ms
    else:
        return None

pctry = vin_det['Plant Country']['value']
pcity = vin_det['Plant City']['value']
pstate = vin_det['Plant State']['value']
pmfr = vin_det['Manufacturer Name']['value']
pmake = vin_det['Make']['value']
pmod = vin_det['Model']['value']
ptype = vin_det['Vehicle Type']['value']

#
def get_related(ctry, city, state, mfr_, make, type):
    relations = {}
    #Other manufacturers in the country
    if get_mfrs_in_country(ctry) is not None:
        names = []
        for mfr in get_mfrs_in_country(ctry):
            names.append(mfrs[mfr_codes[str(mfr)]]['name'])
        relations['mfrs_in_ctry'] = names
    else:
        relations['mfrs_in_ctry'] = []

    #Other manufacturers in the state
    if get_mfrs_in_state(state) is not None:
        names = []
        for mfr in get_mfrs_in_state(state):
            names.append(mfrs[mfr_codes[str(mfr)]]['name'])
        relations['mfrs_in_state'] = names
    else:
        relations['mfrs_in_state'] = []

    #Other manufacturers in the city
    if get_mfrs_in_city(city) is not None:
        names = []
        for mfr in get_mfrs_in_city(city):
            names.append(mfrs[mfr_codes[str(mfr)]]['name'])
        relations['mfrs_in_city'] = names
    else:
        relations['mfrs_in_city'] = []

    #Leader
    if get_leader_by_mfr(mfr_) is not None:
        l_code = get_leader_by_mfr(mfr_)
        mfr_id = leader_codes[str(l_code)]
        relations['leader'] = leaders[mfr_id]
    else:
        relations['leader'] = ''
    #Link to Vin Decoder
    if get_link_by_mfr(mfr_) is not None:
        link_code = get_link_by_mfr(mfr_)
        mfr_id = link_codes[str(link_code)]
        relations['link'] = links[mfr_id]['URL']
    else:
        relations['link'] = ''
    #Manufacturers that share the common name
    #Other makes made by the manufacturer (Sibling makes)
    if get_makes_by_mfr(mfr_) is not None:
        names = []
        for mak in get_makes_by_mfr(mfr_):
            if makes[make_codes[str(mak)]] != make:
                names.append(makes[make_codes[str(mak)]])
        relations['sister_makes'] = names
    else:
        relations['sister_makes'] = []
    #Other makes that make the type of vehicle that the make does
    if get_mfrs_with_same_common_as_(mfr_) is not None:
        relations['same_common_name'] = get_mfrs_with_same_common_as_(mfr_)
    else:
        relations['same_common_name'] = []
    #Models made by the make
    if get_models_by_make(make) is not None:
        names = []
        for mod in get_models_by_make(make):
            names.append(models[model_codes[str(mod)]]['model'])
        relations['models'] = names
    else:
        relations['models'] = []

    return relations

pprint(get_related(ctry=pctry, state=pstate, city=pcity, mfr_=pmfr, make=pmake, type=ptype))







