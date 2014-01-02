import sys
import csv
import urllib2
import pprint
import json

"""
Things you need to do next:
- Convert data types to their proper formats.
e.g coordinates to floats, values to ints.
- Convert to GeoJSON format.
- Add in timestamp

Given remote rows from cso_status_data. Data when downloaded from url 
11TH.CSOSTATUS_N,3
30TH.CSOSTATUS_N,3
3RD.CSOSTATUS_N,3

And local cords in the form of
[{'CSO_TagName': 'ALKI', 'X_COORD': '-122.4225', 'Y_COORD': '47.57024'},
 {'CSO_TagName': 'ALSK', 'X_COORD': '-122.40695', 'Y_COORD': '47.55944'},
 {'CSO_TagName': 'MURR', 'X_COORD': '-122.4', 'Y_COORD': '47.54028'},...]

Create a data structure like
{'Timestamp': '09-25-2013 6:50'
  'Stations' : {
                 'ALKI': { 'x_cord': '-122.3222',
                           'y_cord': '47.57000',
                           'value': 3 }
               }
}

NEED a Data structure template in python to look like this then convert to  GeoJSON 

{'type':'FeatureCollection",
  'features': [{'type': 'Features',
                'properties':{'CSO_TagName': 'ALKI',
                              'Value': 3},
                'geometries':{'type':'point',
                'coordinates':[-122.322,
                              47.607]}              
                }    
               ]   
}
"""

cso_cord = open('partial_coord.csv', 'r')
# MK NOTE: Uncomment below, and comment out above to
# get your command line input back, unless if coordinate data csv data file is in the same directory as
# where python code is.
# cso_cord = open(sys.argv[1])

reader = csv.DictReader(cso_cord)
location = list (reader)
cso_cord.close()

"""Need to convert into this structure 
format_dict = {'type':'FeatureCollection",                                                                  
                'features': [{'type': 'Features','properties':
                                                {'CSO_TagName': 'ALKI'},
                                                'geometries':{'type':'point','coordinates':[-122.322,47.607]}              
                                                }  ]    }
                
keys for this dictionary is ('type' and 'features')

iterate items on format_dict returns following results:
[('type', 'FeatureCollection'), 
  ('features',[{'type': 'Features', 'properties': 
  {'CSO_TagName': 'ALKI'},'geometries': {'type': 'point', 'coordinates': [-122.322, 47607]}}])]

First leave out "Value" using cso_status_csv for now...but just work on 
uisng location to fill out name and coordinates in proper format 

To iterate to add name and coordinates
"""
#formatted_data_dict = {'timestamp': '',
#        'stations': {}}

formatted_data_dict = {'type':'FeatureCollection','features':
[{'type':'Features','properties':{},'geometries':{'type':'point','coordinates':[]}}]}   		                       
#for row in location:
#    format_dict['features']


# Populate with station names and coordinates then converted string into number
#for row in location:
#  formatted_data_dict['features'][row['CSO_TagName']] = {'type':'Features','properties':{},'geometries':{'coordinates':[(row['X_COORD'])],[(row['Y_COORD'])]}}

print(location)
result = json.dumps(formatted_data_dict)
pprint.pprint(result)

#pprint.pprint(formatted_data_dict)

