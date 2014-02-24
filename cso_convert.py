import sys
import csv
import urllib2
import pprint
"""
Things you need to do next:
- Convert data types to their proper formats.
e.g coordinates to floats, values to ints.
- Convert to GeoJSON format.
- Add in timestamp

Given remote rows from cso_status_data
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


Another Option for data strcuture for third table: - having Dictionary with list embded since all 
the data that's coming over will be fixed field data and not mixed

{'Timestamp': '09-25-2013 6:50'
  'Stations' : {
                 'ALKI': ('-122.3222',
                          '47.57000',
                           'value': 3)
               }



"""
# cso_cord is analagous to handle
cso_cord = open('partial_coord.csv', 'r')
# MK NOTE: Uncomment below, and comment out above to
# get your command line input back.
# cso_cord = open(sys.argv[1])

#instead of reading CSV file, it needs to read over CSV from urllib2 methodl
print("the real file")

# Downloading csv status values from the web.
cso_status_data = urllib2.urlopen("http://your.kingcounty.gov/dnrp/library/wastewater/cso/img/CSO.CSV")

# Read CSV into a list
text = cso_status_data.readlines()
cso_status_csv = csv.reader(text)
reader = csv.DictReader(cso_cord)
location = list (reader)
cso_cord.close()

# Setup our ending data format
formatted_data_dict = {'timestamp': '',
                    'stations': {}}

# Populate with staion names and coordinates.
# Need to convert string X_coord & Y_coord into floating number

for row in location:
    formatted_data_dict['stations'][row['CSO_TagName']] = {'X_COORD': row['X_COORD'],
                                                       'Y_COORD': row['Y_COORD']}

# Populate with station values, based on station names.
for line in cso_status_csv:
    cso_name = line[0][0:len(line[0])-12]
    cso_value = line[1]
    # If CSO exists, add to it.
    if cso_name in formatted_data_dict['stations']:
        formatted_data_dict['stations'][cso_name]['value'] = cso_value

pprint.pprint(formatted_data_dict)
