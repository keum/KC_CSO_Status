import sys
import csv
import urllib2
import pprint
import json

cso_cord = open('partial_coord.csv', 'r')
reader = csv.DictReader(cso_cord)
location = list (reader)
cso_cord.close()

formatted_data_dict = {'timestamp': '','stations': {}}

"""this the format we want to output
-question: not sure how to iterate the location object into below formatted_data_dict

formatted_geojson_data_dict = {'type':'FeatureCollection','features':
[{'type':'Features','properties':{},'geometries':{'type':'point','coordinates':[]}}]}


for row in location:
  formatted_geojson_data_dict['features'][row['CSO_TagName']] = {'type':'Features','properties':{},'geometries':{'coordinates':[(row['X_COORD'])],[(row['Y_COORD'])]}}
 """

for row in location:
    formatted_data_dict["stations"][row["CSO_TagName"]] = {"X_COORD": float(row["X_COORD"]),
                                                       "Y_COORD": float(row["Y_COORD"])}

pprint.pprint(formatted_data_dict)