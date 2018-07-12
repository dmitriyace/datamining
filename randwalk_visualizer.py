import matplotlib.pyplot as plt

from random_walk import RandomWalk

# while True:
# creating random walk and putting a dot to a graph
rw = RandomWalk(5000)
rw.fill_walk()
# set window size
plt.figure(figsize=(10, 6))
point_numbers = list(range(rw.num_points))

# plt.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers,
#             cmap=plt.cm.Blues, edgecolor='none')
plt.plot(rw.x_values,rw.y_values,linewidth=1)
# marking first and last points
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
            s=100)
# deleting axis
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
# keep_running = input('make once more? n to stop')
# if keep_running == 'n':
#     break
