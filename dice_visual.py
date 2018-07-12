import pygal
from die import Die

# creating two D6 dice
die_1 = Die()
die_2 = Die(10)

# modeling roll series
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# for frequency in frequencies:
#     print(str(round(frequency/1000*100,2))+"%")

# result visualization
hist = pygal.Bar()

hist.title = "Results of rolling two D6 thousand times"
save_x_labels = []
for value in range(2, max_result+1):
    save_x_labels.append(str(value))
hist.x_labels = save_x_labels
hist._x_title = "Result"
hist._y_title = "Frequency of result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')
print('saved')
