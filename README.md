# Locations for Python

This repo is a duplicate version of my other locations repo written for R. To access mapping tools and the R version, please visit [the originial repository](https://github.com/averymavroudis/locations).

This repo was created to help me learn Python and to make my tools more usable for a variety of crowds. 

### `clustering.py`
Equal to `clustering.R` and `location_csv_writer.R` in one single script. The CSV writer compiles the next most likely location the event may occur by ID number. In order to use, the input CSV must have a list of coordinates associated with an ID number next to it. The columns must be labeled `id`,`latitude`, and `longitude`.

__To Use:__

You have a CSV named __locations.csv__ and you would like a CSV of each ID's next likeliest location. You want to call this CSV __nextLocations.csv__. 

1. You may open the `clustering.py` in Python and run the file to access the function. Then you would enter `locations_csv("locations.csv", "nextLocations.csv")` in your console. __nextLocations.csv__ will be saved in your current working dirctory.
2. From the terminal on your computer, you may enter 
	```
	python cluster.py locations.csv nextLocations.csv
	```
	

