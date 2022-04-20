import json
from pprint import pprint
import requests
import time

base = ""

base = "api/data/"
vin = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/JTDKN3DU7B1398782?format=json&modelyear=2011').json()

vin_det = {}

for r in vin['Results']:
    if r['Value'] is not None and r['Value'] != '' and r['Value'] != 'None':
        vin_det[r['Variable']] = {'id': r['VariableId'], 'value': r['Value']}

<<<<<<< HEAD

with open(f"{base}adj_list.json") as file:
    adj_dict = json.load(file)
    
=======
with open(f"{base}adj_list.json") as file:
    adj_dict = json.load(file)

>>>>>>> c5e0ae209485cbfb7af276dfd3be713eb5990495
with open(f"{base}edge_list.json") as file2:
    edge_dict = json.load(file2)

adj_list = []
for i in range(len(adj_dict)):
    adj_list.append(adj_dict[str(i)])

edge_list = []
for i in range(len(edge_dict)):
    edge_list.append(edge_dict[str(i)])
with open(f"{base}state_codes.json") as sc:
    state_codes = json.load(sc)

with open(f"{base}state_rev.json") as sr:
    state_rev = json.load(sr)

with open(f"{base}ctry_codes.json") as cc:
    ctry_codes = json.load(cc)

with open(f"{base}ctry_rev.json") as cr:
    ctry_rev = json.load(cr)

with open(f"{base}mfr_codes.json") as mc:
    mfr_codes = json.load(mc)

with open(f"{base}mfr_rev.json") as mr:
    mfr_rev = json.load(mr)

with open(f"{base}city_codes.json") as yc:
    city_codes = json.load(yc)

with open(f"{base}city_rev.json") as yr:
    city_rev = json.load(yr)

with open(f"{base}leader_codes.json") as lc:
    leader_codes = json.load(lc)

with open(f"{base}leader_rev.json") as lr:
    leader_rev = json.load(lr)

with open(f"{base}postal_codes.json") as pc:
    postal_codes = json.load(pc)

with open(f"{base}postal_code_rev.json") as pr:
    postal_rev = json.load(pr)

with open(f"{base}common_codes.json") as oc:
    common_codes = json.load(oc)

with open(f"{base}common_rev.json") as o_r:
    common_rev = json.load(o_r)

with open(f"{base}link_codes.json") as ic:
    link_codes = json.load(ic)

with open(f"{base}link_rev.json") as ir:
    link_rev = json.load(ir)

with open(f"{base}make_codes.json") as ac:
    make_codes = json.load(ac)

with open(f"{base}make_rev.json") as ar:
    make_rev = json.load(ar)

with open(f"{base}model_codes.json") as dc:
    model_codes = json.load(dc)

with open(f"{base}model_rev.json") as dr:
    model_rev = json.load(dr)

with open(f"{base}type_codes.json") as tc:
    type_codes = json.load(tc)

with open(f"{base}type_rev.json") as tr:
    type_rev = json.load(tr)

with open(f"{base}code_master.json") as file3:
    master_codes = json.load(file3)

with open(f"{base}mfr_by_name.json") as nf:
    mfr_name = json.load(nf)

with open(f"{base}makes_by_name.json") as nf:
    make_name = json.load(nf)

with open(f"{base}type_name.json") as nf:
    type_name = json.load(nf)

with open(f"{base}new_mfrs.json") as file:
    mfrs = json.load(file)

with open(f"{base}leaders.json") as file3:
    leaders = json.load(file3)

with open(f"{base}links.json") as file7:
    links = json.load(file7)

with open(f"{base}new_makes.json") as file5:
    makes = json.load(file5)

with open(f"{base}new_models.json") as file2:
    models = json.load(file2)

with open(f"{base}type_name_flipped.json") as file6:
    type_name_flipped = json.load(file6)

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

def get_mfrs_in_postal(postal):
    if postal_rev.get(postal) is not None:
        postal_code = int(postal_rev[postal])
        nodes = adj_list[postal_code]

        mfrs = set()
        leaders = []

        for n in nodes:
            if 10208 <= n <= 29207:
                leaders.append(n)

            for leader in leaders:
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

        postals = 0

        for n in nodes:
            if 93970 <= n <= 104923:
                postals = n

        if postals == 0:
            return None

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
                ms.append(mfrs[mfr_codes[str(m)]]['name'])

        return ms
    else:
        return None

def get_types_by_make(make):
    mk = make_name[make]
    mk_code = make_rev[mk]
    types = set()
    for t in adj_list[int(mk_code)]:
        if 93961 <= t <= 93969:
            types.add(t)

    tipos = []

    if len(types) == 0:
        return None
    else:
        for t in types:
            tipos.append(type_name_flipped[str(type_codes[str(t)])])

    return tipos

def get_makes_with_same_type(make):
    t_codes = []

    for t in get_types_by_make(make):
        t_codes.append(type_rev[str([type_name[t]][0])])

    tm = {}

    for t in t_codes:
        tm[type_name_flipped[str(type_codes[t])]] = f"{len(adj_list[int(t)])} manufacturers"

    if len(tm) == 0:
        return None
    else:
        return tm

pctry = vin_det['Plant Country']['value']
pcity = vin_det['Plant City']['value']
pstate = vin_det['Plant State']['value']
pmfr = vin_det['Manufacturer Name']['value']
pmake = vin_det['Make']['value']
pmod = vin_det['Model']['value']
ptype = vin_det['Vehicle Type']['value']

<<<<<<< HEAD
#
def get_related(ctry, city, state, mfr_, make):
=======
#print(pctry, pcity, pstate, pmfr, pmake, pmod, ptype)

def get_related_adj(ctry, city, state, mfr_, make, type_):
    start = time.time()

>>>>>>> c5e0ae209485cbfb7af276dfd3be713eb5990495
    relations = {}
    #Other manufacturers in the country
    if get_mfrs_in_country(ctry) is not None:
        names = []
        for mfr in get_mfrs_in_country(ctry):
            names.append(mfrs[mfr_codes[str(mfr)]]['name'])
        relations['mfrs_orig_from_ctry'] = names
    else:
        relations['mfrs_orig_from_ctry'] = []

    #Other manufacturers in the state
    if get_mfrs_in_state(state) is not None:
        names = []
        for mfr in get_mfrs_in_state(state):
            names.append(mfrs[mfr_codes[str(mfr)]]['name'])
        relations['mfrs_orig_from_state'] = names
    else:
        relations['mfrs_orig_from_state'] = []

    #Other manufacturers in the city
    if get_mfrs_in_city(city) is not None:
        names = []
        for mfr in get_mfrs_in_city(city):
            names.append(mfrs[mfr_codes[str(mfr)]]['name'])
        relations['mfrs_orig_from_city'] = names
    else:
        relations['mfrs_orig_from_city'] = []

    #Other manufacturers in the postal
    if get_postal_by_mfr(mfr_) is not None:
        postal = get_postal_by_mfr(mfr_)
        if get_mfrs_in_postal(postal):
            names = []
            for mfr in get_mfrs_in_postal(postal):
                names.append(mfrs[mfr_codes[str(mfr)]]['name'])
        relations['mfrs_orig_from_postal'] = names
    else:
        relations['mfrs_orig_from_postal'] = []

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
    if get_mfrs_with_same_common_as_(mfr_) is not None:
        relations['same_common_name'] = get_mfrs_with_same_common_as_(mfr_)
    else:
        relations['same_common_name'] = []

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
    if get_types_by_make(make) is not None:
        relations['types_produced'] = get_types_by_make(make)
    else:
        relations['types_produced'] = []

    #Models made by the make
    if get_models_by_make(make) is not None:
        names = []
        for mod in get_models_by_make(make):
            names.append(models[model_codes[str(mod)]]['model'])
        relations['models'] = names
    else:
        relations['models'] = []

    # Makes that produce the same types of cars
    if get_makes_with_same_type(make) is None:
        relations['other_man_types'] = {}
    else:
        relations['other_man_types'] = get_makes_with_same_type(make)

    end = time.time()

    relations['elapsed_time'] = f"{(end-start)*1000} milliseconds"

    return relations

def get_related_edge(ctry, city, state, mfr_, make, type_):
    None

pprint(get_related_adj(ctry=pctry, state=pstate, city=pcity, mfr_=pmfr, make=pmake, type_=ptype))

