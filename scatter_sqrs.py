import matplotlib.pyplot as plt
import time
squares = []
values = range(0, 1001)
squares = [x ** 2 for x in values]
plt.scatter(values, squares, c=squares, cmap=plt.cm.Blues, edgecolor='none',
            s=40)

# setting title od diagram and axes lables
plt.title("Square nums", fontsize=16)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of Value", fontsize=12)
# setting fontsize of axes delimiters (ticks)
plt.tick_params(axis='both', which='major', labelsize=12)
# setting range for every axis
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plt_'+str(time.time())+'.png', bbox_inches = 'tight')
