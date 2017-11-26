import pygal

from die import Die

die1 = Die(8)
die2 = Die(8)

results = []
for roll_num in range(1000000):
	result = die1.roll() + die2.roll()
	results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling two D8 100000 times."
hist.x_labels = list(range(2, max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D8 + D8", frequencies)
hist.render_to_file('dice_visual_8.svg')

print(frequencies)
