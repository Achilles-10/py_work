import pygal

from die import Die

die1 = Die()
die2 = Die()
die3 = Die()

results = []
for roll_num in range(5000):
	result = die1.roll() + die2.roll() + die3.roll()
	results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(3, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling three D6 5000 times."
hist.x_labels = list(range(3, max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file('dice_triple_visual.svg')

print(frequencies)
