KC_CSO_Status
=============

Summary: 
Take KC CSOs status data from server and join CSV table with long/lat coordinates. Transform this table into geojson format then post the data onto GitHub site to view the map. Using python to join and tranform into geojson then upload onto GitHub repository to view the map.

Purpose: Map project to display real-time status of KC CSO

Workflow

1. Created CSO name and location in WGS84 coordinate with longitude and latitude
Locally created File - cso_coord.csv

2. Download CSV file that contains CSO status condition and name from this site:
http://your.kingcounty.gov/dnrp/library/wastewater/cso/img/CSO.CSV 

Status condition 
    1 = Red, CSO discharging now
    2 = Yellow, CSO discharged in last 48 hrs
    3 = Green, CSO not discharging
    4 = Blue, Real time data not available
   

3.Join these two tables into one table.
4. Convert this table into geoJSON format. 
5. Push this table into GitHub repositiory



