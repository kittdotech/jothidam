import os
import json

house_map = {
  "0": "0_1",
  "1": "0_2",
  "2": "0_3",
  "3": "1_3",
  "4": "2_3",
  "5": "3_3",
  "6": "3_2",
  "7": "3_1",
  "8": "3_0",
  "9": "2_0",
  "10": "1_0",
  "11": "0_0"
}

def new_chart():
	return {
	  "0": {
	    "name": "Mesham",
	    "planets": [],
	    "astavarga_point": 0
	  },
	  "1": {
	    "name": "Rishabam",
	    "planets": [],
	    "astavarga_point": 0
	  },
	  "2": {
	    "name": "Mithunam",
	    "planets": [],
	    "astavarga_point": 0
	  },
	  "3": {
	    "name": "Katagam",
	    "planets": [],
	    "astavarga_point": 0
	  },
	  "4": {
	    "name": "Simam",
	    "planets": [],
	    "astavarga_point": 0
	  },
	  "5": {
	    "name": "Kanni",
	    "planets": [],
	    "astavarga_point": 0
	  },
	  "6": {
	    "name": "Thulam",
	    "planets": [],
	    "astavarga_point": 0
	  },
	  "7": {
	    "name": "Viruchagam",
	    "planets": [],
	    "astavarga_point": 0
	  },
	  "8": {
	    "name": "Thanusu",
	    "planets": [],
	    "astavarga_point": 0
	  },
	  "9": {
	    "name": "Makaram",
	    "planets": [],
	    "astavarga_point": 0
	  },
	  "10": {
	    "name": "Kumbam",
	    "planets": [],
	    "astavarga_point": 0
	  },
	  "11": {
	    "name": "Meenum",
	    "planets": [],
	    "astavarga_point": 0
	  }
	}

def astavarga_planets():
  return ["Sun", "Moon", "Mars", "Venus", "Jupiter", "Mercury", "Saturn"];


def load_planets_point():
  json_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'planet_points.json')
  with open(json_path) as f:
    return json.load(f)

def generate_astavarga(rasi_chart):
	astavarga_charts = {}
	for planet in astavarga_planets():
		# Create new chart for astavarga planets
		astavarga_charts[planet] = calculate_binastavarga(planet, rasi_chart)
	astavarga_charts['SAV'] = calculate_sarva_astakavarga(astavarga_charts)
	return astavarga_charts

def calculate_binastavarga(planet, rasi_chart):
    astavarga_table = load_planets_point()
    astavarga_chart_for_planet = new_chart()
    for sub_planet in astavarga_table[planet]:
      sub_planet_position = planet_position_in_chart(planet, rasi_chart)
      sub_planet_points = astavarga_table[planet][sub_planet]
      for position in sub_planet_points:
        target_position = (int(sub_planet_position) + int(position) - 1) % 12
        astavarga_chart_for_planet[str(target_position)]['astavarga_point'] += 1
    return astavarga_chart_for_planet

def calculate_sarva_astakavarga(astavarga_charts):
    sarva_astavarga_chart = new_chart()
    for planet in astavarga_charts:
      for position in astavarga_charts[planet]:
         sarva_astavarga_chart[position]['astavarga_point'] += astavarga_charts[planet][position]['astavarga_point']
    return sarva_astavarga_chart

def planet_position_in_chart(planet, rasi_chart):
	for position in rasi_chart:
		if planet in rasi_chart[position]['planets']:
			return position
