import pygal
from die import Die

# creating D6 die (die which has 6 facets)
die = Die()

# modeling roll series
results=[]
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
frequencies=[]
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency/1000*100)

# for frequency in frequencies:
#     print(str(round(frequency/1000*100,2))+"%")

# result visualization
hist = pygal.Bar()

hist.title = "Results of rolling one D6 thousand times"
hist.x_labels = ['1','2','3','4','5','6']
hist._x_title = "Result"
hist._y_title = "Frequency of result"

hist.add('D6', frequencies)
hist.render_to_file('sie_visual.svg')