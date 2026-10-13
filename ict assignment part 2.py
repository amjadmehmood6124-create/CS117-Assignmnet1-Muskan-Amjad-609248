current = int(input("Enter a value of current: "))
if (current == 0):
    print("No current flows")
elif (current > 0):
    print("Current flows from A to B")
else:
    print("Current flows from B to A")
