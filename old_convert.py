import sys
import csv
import urllib2
import pprint

#f = open('/Users/peter/Documents/CSO/cso_status.dat', 'w')
handle = open (sys.argv[1])

#instead of reading CSV file, it needs to read over CSV from urllib2 methodl
"""print("the real file")

page = urllib2.urlopen("http://your.kingcounty.gov/dnrp/library/wastewater/cso/img/CSO.CSV")

text =page.read().decode('utf8')

print(text)"""

reader = csv.DictReader(handle)
location = list (reader)
handle.close()



#for column in location:
#	print column['CSO_TagName']

pprint.pprint(location)

#f.write(','.join(location))

#f.close()


# Need to add additional key & value to location file


