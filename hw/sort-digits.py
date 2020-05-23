#!/usr/bin/python3

# Examples
# 8970 --> 789
# 32445 --> 23445
# 10101 --> 111


def sort_digits(n):
    freqs = [0 for _ in range(10)]
    while n > 0:
        freqs[n % 10] += 1
        n //= 10
    all_digits = []
    for i in reversed(range(1, 10)):
        if freqs[i] > 0:
            all_digits.extend(freqs[i] * [i])
    for i in range(len(all_digits)):
        n += (10 ** i) * all_digits[i]
    return n

print(sort_digits(8970))
