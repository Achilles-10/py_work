import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#336699', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Python projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dict = [
	{'value': 16101, 'label': 'Description of httpie.'},
	{'value': 15028, 'label': 'Description of django.'},
	{'value': 14798, 'label': 'Description of flask.'}
]

chart.add('', plot_dict)
chart.render_to_file('bar_descriptions.svg')
