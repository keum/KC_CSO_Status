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

And local cords in the form of
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

# Downloading csv status values from the web.
cso_status_data = urllib2.urlopen("http://your.kingcounty.gov/dnrp/library/wastewater/cso/img/CSO.CSV")

# Read CSV into a list
text = cso_status_data.readlines()
cso_status_csv = csv.reader(text)
pprint.pprint(cso_status_csv)


#Reading CSO with Coordinate in csv file locally and create list, subtitue with full data
cso_cord = open('partial_coord.csv', 'r')
reader = csv.DictReader(cso_cord)
location = list (reader)
cso_cord.close()










