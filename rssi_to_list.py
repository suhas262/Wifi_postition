import json

from pprint import pprint

with open('testJson.txt') as data_file:
	data = json.load(data_file)

list_map = []

for value in data:
	map_rssi = ( value["mac"].encode('ascii','ignore'), value["rssi"] )
	list_map.append(map_rssi)

print list_map
