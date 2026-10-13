voltage = int(input("Enter the voltage: "))
resistance = int(input("Enter the resistance: "))
current_I = voltage/resistance
if (resistance <= 0):
    print("invalid resistance.")
else:
    current_I = voltage / resistance
    if (current_I > 2):
        print("Fuse will blow.")
    else:
        print("Circuit is safe.")
