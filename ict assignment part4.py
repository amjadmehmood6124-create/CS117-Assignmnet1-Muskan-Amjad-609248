bit1 = int(input("Enter A: "))
bit2 = int(input("Enter B: "))
if bit1 not in (0, 1) or bit2 not in (0, 1):
    print("Bits must be 0 or 1")
else:
    AND_result = bit1 and bit2
    OR_result = bit1 or bit2
    XOR_result = bit1 ^ bit2
    print("AND = ", AND_result)
    print("OR = ", OR_result)
    print("XOR = ", XOR_result)
