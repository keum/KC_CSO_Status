#peter remove, not used# import sys
#peter remove, not used# import os
import subprocess
import time
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
Input data in csv strcture and output data structure in geojson format.

Given remote rows from cso_status_data. Data when downloaded from FTP url site.
Example Data:
11TH.CSOSTATUS_N,3
30TH.CSOSTATUS_N,3
3RD.CSOSTATUS_N,3

And cso_coord.csv in the form of
[{'CSO_TagName': 'ALKI', 'X_COORD': '-122.4225', 'Y_COORD': '47.57024', 'Name':'Alki, 'DSN':'051'},
 {.......}]


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

# Read csv file into a python list named cso_status_csv
text = cso_status_data.readlines()  #reading each line of downloaded csv file
cso_status_csv = csv.reader(text)   #creating new object call cso_status_csv from CSV file from url
#debug# pprint.pprint(cso_status_csv)


#Reading CSO with Coordinate in csv file locally and create list,
#subtitue with full data file cso_coord.csv or partial_coord.csv for two point data
cso_cord = open('cso_coord.csv', 'r')
reader = csv.DictReader(cso_cord)

location = list (reader)
cso_cord.close()
#debug# pprint.pprint(location)


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
                                                        'DSN':row['DSN'],
                                                        'Name':row['Name'],
                                                        'Time_stamp':time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime()),
                                                        'Location':"%1.3f , %1.3f" % (float(row["X_COORD"]) ,float(row["Y_COORD"])),
                                                        'CSO_Status':0,'marker-color':'#666',
                                                        'marker-size':'small',
                                                        'marker-symbol':'circle',
                                                        'description':'No Data Available'},
                                          'geometry':{'type':'Point',
                                                      'coordinates':[float(row["X_COORD"]), float(row["Y_COORD"])]
                                                     }
                                          })


#create brand new dictionary style with color according to that status
# Value 1 = #DC143C Discharging now
# Value 2 = #FFD700 Discharged last 48 hrs
# Value 3 = #00CD00 Not Discharging
# Value 4 = #0000EE No Real Time Data

style_dict = {"1":{'marker-color':'#DC143C','marker-size':'small','description':'Discharging'},
              "2":{'marker-color':'#FFD700','marker-size':'small','description':'Discharge 48 hrs'},
              "3":{'marker-color':'#00CD00','marker-size':'small','description':'No Discharge'},
              "4":{'marker-color':'#0000EE','marker-size':'small','description':'No Real Time Data'}


              }

#??? - Not sure how to add value to be added onto geojson_data_dict object, replace with
##default vaue of 0........
"""Paul M. helped to crated loop to add CSO_Status value
(geojson_data_dict['features'][0]) is dict
and print it returns
{'geometry':{coordinates':[-122.4225,47.57024],'type':Point'},
'properties':{'CSO_Status':0,'CSO_TagName':'ALKI'},'type':'Feature'}

Replace geojson_data_dict's one of the value with CSO status. Refer to the note.

"""


# Populate with station values, based on station names.
for line in cso_status_csv:
    #Test to see record is in Seattle CSO data or not
    if line[0][0:5]=="NPDES": # this indicates the data is Seattle CSO
        cso_name = line[0]
        cso_symbol = 'x' #indicate Seattle CSO
    else: #this is not Seattle CSO and is for King County CSO
        cso_name = line[0][0:len(line[0])-12]
        cso_symbol = 'circle' # this indicates KC CSO
    #for all records
    CSO_Status = line[1]
    # If CSO exists, add to it.
    #Iterate through 'features' list
    for element in geojson_data_dict['features']:
      if cso_name == element['properties']['CSO_TagName']:
        element['properties']['CSO_Status'] = CSO_Status
        #element['properties'].append(style_dict[CSO_Status])
        element['properties']['marker-color']=style_dict[CSO_Status]['marker-color']
        element['properties']['marker-size']=style_dict[CSO_Status]['marker-size']
        element['properties']['description']=style_dict[CSO_Status]['description']
        #adding new element with symbol specific to seattle and KC
        element['properties']['marker-symbol']=cso_symbol

 #write out same element with additional style properties

formatted_geojson_data_dict = json.dumps(geojson_data_dict)
pprint.pprint(formatted_geojson_data_dict)


#take formatted_geojson_data_dict file and convert '' string into a file using with open
#out_file_fullpath ='/Users/peter/Documents/KC_CSO_Status/test_file5_5.geojson'

#take formatted_geojson_data_dict file and convert '' string into a file using with open down is for windows


#out_file_fullpath ='/Users/keump/Documents/GitHub/KC_CSO_Status/test_file.geojson' #for Windows 7

# file for public repo for Windows machine
out_file_fullpath = '/Users/keump/Documents/GitHub/data_display/cso_test_file.geojson'

# directory for public repo
out_file_fullpath_directory = '/Users/keump/Documents/GitHub/data_display'

# file for public repo for OS machine
#out_file_fullpath ='/Users/peter/Documents/KC_CSO_Status/test_file.geojson' #for macbook


with open(out_file_fullpath, 'w') as out_file:
   out_file.write(formatted_geojson_data_dict)


#using subprocess module to push the data into GitHub site to be view

subprocess.call(['git', '--git-dir', out_file_fullpath_directory + '/.git',
                '--work-tree', out_file_fullpath_directory,
                'add', out_file_fullpath])
subprocess.call(['git', '--git-dir', out_file_fullpath_directory  +'/.git',
                '--work-tree', out_file_fullpath_directory,
                'commit', '-a', '-m', '"Data Upload: ' + time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime()) + '"'])
subprocess.call(['git', '--git-dir', out_file_fullpath_directory + '/.git',
                '--work-tree', out_file_fullpath_directory,
                'push'])

