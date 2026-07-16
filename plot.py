# Line plot for 2 weeks of wind in Washington

import matplotlib.pyplot as plt
import statistics

days = ["16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]
mph = [10, 7, 9, 9, 8, 7, 7, 6, 7, 7, 7, 7, 7, 7]

plt.plot(days, mph, marker = 'o', color = 'black', linestyle = '-')

plt.title("Weekly wind gusts in Washington")
plt.xlabel("July")
plt.ylabel("Gusts (mph)")

plt.ylim(0, 11)
plt.yticks(range(0, 11))

plt.grid(True)

mean_value = statistics.mean(mph)
average = round(mean_value)
print("The average wind gust for a week in Washington is: ", average, "mph")

plt.show()