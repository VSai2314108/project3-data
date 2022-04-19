import json
import pprint

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



