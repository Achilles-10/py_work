import pygal

from die import Die

die1 = Die()
die2 = Die(10)

results = []
for roll_num in range(50000):
	result = die1.roll() + die2.roll()
	results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = list(range(2,17))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D10", frequencies)
hist.render_to_file('different_dice_visual.svg')

print(frequencies)
