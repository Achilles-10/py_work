from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'North, Central, an South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'pa', 'sv'])
wm.add('South America',
       ['ar', 'bo', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('america.svg')