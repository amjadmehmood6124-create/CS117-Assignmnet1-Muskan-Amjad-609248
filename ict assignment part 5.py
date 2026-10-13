R1 = int(input("Enter R1: "))
R2 = int(input("Enter R2: "))
R3 = int(input("Enter R3: "))
if R1<R2 and R1<R3:
    print("Smallest =", R1, "ohm")
elif R2<R1 and R2<R3:
    print("Smallest =", R2, "ohm")
else:
    print("Smallest =", R3, "ohm")
if R1>R2 and R1>R3:
    print("Largest =", R1, "ohm")
elif R2>R1 and R2>R3:
    print("Largest =", R2, "ohm")
else:
    print("Largest =", R3, "ohm")
