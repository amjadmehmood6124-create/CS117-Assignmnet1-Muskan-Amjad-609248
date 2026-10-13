def parallel_resistance(resistors):
    total = 0
    for r in resistors:
        total = total + (1/r)
    return 1 / total
result_1 = parallel_resistance([20, 40])
result_2 = parallel_resistance([200, 400, 600])
print("parallel_resistance([20, 40]) ->", round(result_1, 2))
print("parallel_resistance([200, 400, 600]) ->", round(result_2, 2))
