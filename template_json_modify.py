import sys
import csv
import urllib2
import pprint
import json

cso_cord = open('partial_coord.csv', 'r')
reader = csv.DictReader(cso_cord)
location = list (reader)
cso_cord.close()

"""this the format we want to output
-question: not sure how to iterate the location object into below formatted_data_dict

formatted_geojson_data_dict = {'type':'FeatureCollection','features':
[{'type':'Feature','properties':{},'geometry':{'type':'Point','coordinates':[]}}]}


for row in location:
  formatted_geojson_data_dict['features'][row['CSO_TagName']] = 
  		{'type':'Feature',
  		'properties':{},
  		'geometry':{'coordinates':[(row['X_COORD'])],[(row['Y_COORD'])]}}
 """

geojson_data_dict = {'type':'FeatureCollection','features':[]}

for row in location:
    # We want to populate this stub, for every row, in the location list
    # {'type':'Features','properties':{},'geometry':{'type':'Point','coordinates':[]}}
    geojson_data_dict['features'].append({'type':'Feature',
                                          'properties':{'CSO_TagName':row['CSO_TagName'],
                                                        'Value':0},
                                          'geometry':{'type':'Point',
                                                      'coordinates':[float(row["X_COORD"]), float(row["Y_COORD"])]
                                                     }
                                          })
"""  
modified to work w/ above code...to   
# Populate with station values, based on station names.
for line in cso_status_csv:
    cso_name = line[0][0:len(line[0])-12]
    cso_value = line[1]
    # If CSO exists, add to it.
    if cso_name in formatted_data_dict["stations"]:
        formatted_data_dict["stations"][cso_name]["value"] = cso_value
"""



formatted_geojson_data_dict = json.dumps(geojson_data_dict)
pprint.pprint(formatted_geojson_data_dict)