voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
max_length = 0
start_voltage = 0
end_voltage = 0
current_length = 1
current_start = voltages[0]
for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        if current_length == 1:
            current_start = voltages[i - 1]
        current_length += 1
        current_end = voltages[i]
    else:
        current_length = 1
        current_start = voltages[i]
    if current_length > max_length:
        max_length = current_length
        start_voltage = current_start
        end_voltage = current_end
print("Longest continuous drop:", max_length, "minutes")
print("started at:", start_voltage, "V")
print("Ended at:", end_voltage, "V")
