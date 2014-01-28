KC_CSO_Status
=============

Summary: 
Take KC CSOs status data from server and join CSV table with long/lat coordinates. Transform this table into geojson format then post the data onto GitHub site to view the map. Using python to join and tranform into geojson then upload onto GitHub repository to view the map.

Purpose: Map project to display real-time status of KC CSO

Workflow

* Created CSO name and location in WGS84 coordinate with longitude and latitude

Locally created File:- cso_coord.csv

* Download CSV file that contains CSO status condition and name from this site:
http://your.kingcounty.gov/dnrp/library/wastewater/cso/img/CSO.CSV 

Status condition 
    1 = Red, CSO discharging now<br>
    2 = Yellow, CSO discharged in last 48 hrs<br>
    3 = Green, CSO not discharging<br>
    4 = Blue, Real time data not available <br>
   

* Join these two tables into one table.

* Convert this table into geoJSON format. 

* Push this table into GitHub repositiory

File Description:

old_convert.py = very first simple python script to read CSV file from Web site

cso_convert.py = script to download CSV file from the data website and crate data dictionary

partial_code.py = old archieve script trying to convert result from cso_convert.py (data dictionary) into geoJSON format but does not work.

template_json_modify.py = next version of cso_convert.py that reformatted results from cso_convert.py (data dictionay) into geoJSON format successfully. Able to convert into geoJSON format with hardcoded example, need to be replaced with CSV file from the web and combine from data dictionary. 


