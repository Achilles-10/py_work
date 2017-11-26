import pygal

from die import Die

die1 = Die()
die2 = Die()

results = []
for roll_num in range(50000):
	result = die1.roll() * die2.roll()
	results.append(result)

frequencies = []
x_label = []
max_result = die1.num_sides * die2.num_sides
for x in range(1, die1.num_sides+1):
	for y in range(1,die2.num_sides+1):
		if x * y not in x_label:
			x_label.append(x * y)
			frequency = results.count(x*y)
			frequencies.append(frequency)


hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = x_label
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 * D6", frequencies)
hist.render_to_file('test.svg')

print(frequencies)
