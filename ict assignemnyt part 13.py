def decimal_to_binary(n):
    if n == 0:
        return "0"
    remainders = []
    while n > 0:
        rem = n % 2
        remainders.append(rem)
        n = n // 2
    binary_str = ""
    i = len(remainders) - 1
    while i >= 0:
        binary_str = binary_str + str(remainders[i])
        i = i - 1
    return binary_str
result_1 = decimal_to_binary(20)
result_2 = decimal_to_binary(35)
print("decimal_to_binary(20) ->", result_1)
print("decimal_to_binary(35) ->", result_2)
