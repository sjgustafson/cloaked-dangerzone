
import requests

def filter_stations(line):
	label = line[5:9]
	Lat = float(line[36:41])
	Lon = -float(line[46:51])
	return label, Lat, Lon
	
def test_filter_stations():
	assert filter_stations(' 8   K1H2 EFFINGHAM CNTY MEM   IL   39.07N    88.53W') == ('K1H2', 39.07, -88.53)
	assert filter_stations(' 8   KFOA FLORA MUNI AIRPORT   IL   38.66N    88.45W') == ('KFOA', 38.66, -88.45)
	assert filter_stations(' 8   KETB WEST BEND            WI   43.42N    88.13W') == ('KETB', 43.42, -88.13)






def main():
	data = requests.get('http://www.nws.noaa.gov/mdl/gfslamp/docs/stations_info.shtml')

	for line in data.text.splitlines():
		if ' IL ' in line: 
			filter_stations(line)
			print (line)

if __name__ == '__main__':
	#main()
	test_filter_stations()
