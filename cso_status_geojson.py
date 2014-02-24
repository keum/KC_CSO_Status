import sys
import csv
import urllib2
import pprint
import json


"""
Take status csv file from url and coordinate csv file to create 
data dictionary format and convert that format into geojson type. 
This geojson data can then be loaded into GitHub page to view
using it's mapping component

"""

"""
Input data strcture and output data structure (geojson)

Given remote rows from cso_status_data. Data when downloaded from url 
11TH.CSOSTATUS_N,3
30TH.CSOSTATUS_N,3
3RD.CSOSTATUS_N,3

And local coords in the form of
[{'CSO_TagName': 'ALKI', 'X_COORD': '-122.4225', 'Y_COORD': '47.57024'},
 {'CSO_TagName': 'ALSK', 'X_COORD': '-122.40695', 'Y_COORD': '47.55944'},
 {'CSO_TagName': 'MURR', 'X_COORD': '-122.4', 'Y_COORD': '47.54028'},...]


formatted_geojson_data_dict = {'type':'FeatureCollection','features':
[{'type':'Feature','properties':{},'geometry':{'type':'Point','coordinates':[]}}]}

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

# Downloading csv status values from the web, ftp site.
cso_status_data = urllib2.urlopen("http://your.kingcounty.gov/dnrp/library/wastewater/cso/img/CSO.CSV")

# Read csv file into a python list name cso_status_csv
text = cso_status_data.readlines()
cso_status_csv = csv.reader(text)
#pprint.pprint(cso_status_csv)


#Reading CSO with Coordinate in csv file locally and create list, 
#subtitue with full data later
cso_cord = open('partial_coord.csv', 'r')
reader = csv.DictReader(cso_cord)

location = list (reader)
cso_cord.close()
#pprint.pprint(location)


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

#Create dictionary with geojson template
geojson_data_dict = {'type':'FeatureCollection','features':[]}


for row in location:
    # We want to populate this stub, for every row, in the location list
    # {'type':'Features','properties':{},'geometry':{'type':'Point','coordinates':[]}}
    geojson_data_dict['features'].append({'type':'Feature',
                                          'properties':{'CSO_TagName':row['CSO_TagName'],
                                                        'CSO_Status':0},
                                          'geometry':{'type':'Point',
                                                      'coordinates':[float(row["X_COORD"]), float(row["Y_COORD"])]
                                                     }
                                          })


  

#??? - Not sure how to add value to be added onto geojson_data_dict object, replace with 
##default vaue of 0........
"""with help from Paul, 
(geojson_data_dict['features'][0]) is dict
and print it returns
{'geometry':{coordinates':[-122.4225,47.57024],'type':Point'},
'properties':{'CSO_Status':0,'CSO_TagName':'ALKI'},'type':'Feature'}

"""



# modified to work w/ above code...to   
# Populate with station values, based on station names.
for line in cso_status_csv:
    cso_name = line[0][0:len(line[0])-12]
    CSO_Status = line[1]
    # If CSO exists, add to it.
    if cso_name in geojson_data_dict['features']:
        geojson_data_dict['features'][cso_name]['value'] = cso_value
 
       

formatted_geojson_data_dict = json.dumps(geojson_data_dict)
pprint.pprint(formatted_geojson_data_dict)







