import csv
from matplotlib import pyplot as plt
from datetime import datetime

# reading max_temerature and dates from csv
filename = "sitka_weather_07-2014.csv"
dates, highs, lows = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)

# putting data on the diagram
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue',alpha=0.1)
# diagram formatting
plt.title("Daily high 'n low temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
# for index, column_header in enumerate(header_row):
#     print(index, column_header)
