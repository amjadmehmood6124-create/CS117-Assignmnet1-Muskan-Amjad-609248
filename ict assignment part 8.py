readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
above_count = 0
total_sum = 0
highest = readings[0]
lowest = readings[0]
total_readings = 0
for v in readings:
    if v > 3.2:
        above_count = above_count + 1
    total_sum = total_sum + v
    total_readings = total_readings + 1
    if v > highest:
        highest = v
    if v < lowest:
        lowest = v
average = total_sum / total_readings
print("Readings above 3.2 V:", above_count)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print("Average:", round(average, 2), "V")
