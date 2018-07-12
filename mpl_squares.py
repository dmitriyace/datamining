import matplotlib.pyplot as plt

squares = []
for num in range(-11, 12):
    squares.append(num * num)
plt.plot(range(-11,12),squares, linewidth=5)
# name of diagram title and axes' labels
plt.title("Squares", fontsize = 24)
plt.xlabel("Value", fontsize = 12)
plt.ylabel("Square", fontsize = 12)
# setting font size and axes division
plt.tick_params(axis='both', labelsize = 10)

plt.show()
