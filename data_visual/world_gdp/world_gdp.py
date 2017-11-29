import json

from pygal.style import RotateStyle, LightColorizedStyle
from country_code import get_country_code
from pygal.maps.world import World

filename = 'world_gdp.json'
with open(filename) as f:
	gdp_data = json.load(f)

cc_gdps = {}
for gdp_dict in gdp_data:
	if gdp_dict['Year'] == 2010:
		country_name = gdp_dict['Country Name']
		gdp = int(gdp_dict['Value'])
		code = get_country_code(country_name)
		if code:
			cc_gdps[code] = gdp

cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for cc, gdps in cc_gdps.items():
	if gdps < 5e+10:
		cc_gdp_1[cc] = gdps
	elif gdps < 3e+12:
		cc_gdp_2[cc] = gdps
	else:
		cc_gdp_3[cc] = gdps

wm = World()
wm_style = RotateStyle('#ff3333',base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = "World GDP in 2010, by Country"
wm.add(">3e+12", cc_gdp_3)
wm.add("5e+10 - 3e+12", cc_gdp_2)
wm.add("0 - 5e+10", cc_gdp_1)

wm.render_to_file("world_gdp.svg")
