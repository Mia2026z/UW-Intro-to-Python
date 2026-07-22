import statistics

numbers = [9, 11, 9, 13, 8]

mean = statistics.mean(numbers)

print("The mean of this data set is:", mean, "inches")

median = statistics.median(numbers)
print("The median of this data set is:", median, "inches")

mode = statistics.mode(numbers)
print("The mode of this data set is:", mode, "inches")


class_data = {"Math": 16, 
              "Science": 8, 
              "English": 2, 
              "History": 1, 
              "Economics": 1, 
              "Music Theory": 2
              }

mode_class = statistics.mode(class_data)
print("Mode is:", mode_class)
