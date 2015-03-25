KC_CSO_Status
=============

Summary:

Starting with King County Combined Sewer Overflow (CSO) status data publicly available from the web, join to a CSV table that contains longitude/latitude coordinates. Export the joined data as text in the geojson format, and post the data to GitHub. The data can be viewed on a basemap directly on GitHub. Additionaly the geojson file is made available using GitHub GH-Pages functionality to be consumed by JavaScript based web pages.

Purpose:

Provide a web map that displays the real-time status of King County CSO sites.

Data Resources:

cso_coord.csv - A file located in this respository that contains a WGS84 coordinate pair, a site name, and a DSN for each of the CSO sites.

http://your.kingcounty.gov/dnrp/library/wastewater/cso/img/CSO.CSV - publicly available data that contains a status condition and name for each of the CSO sites.

Lookup tables for tatus conditions (currently hard coded in python script) <br>
    1 = Red, CSO discharging now Hex code = #DC143C<br>
    2 = Yellow, CSO discharged in last 48 hrs Hex code = #FFD700<br>
    3 = Green, CSO not discharging Hex code = #00CD00<br>
    4 = Blue, Real time data not available Hex code = #0000EE<br>

Workflow:

* Created CSO name and location in WGS84 coordinate with longitude and latitude

* Join these two tables into one table, create dictionary table in python

* Convert this table into geoJSON format and add style according to it's status value

* Push this table into GitHub data_display repositiory: https://github.com/keum/data_display

Code Files:

cso_status_geojson.py = main program that accomplishes the workflow described above.

Future Developments:

* Remove marker style attributes from GeoJSON to allow formatting to be separated from the data and be coded in JavaScript on the final web map.

* Consider moving output data into this repository rather than outputting to separate repository. Considering costs and benefits.