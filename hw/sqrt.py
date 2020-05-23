#!/usr/bin/python3

def square_root(n):
    lo, hi, result = 0, n, n / 2
    while abs(result ** 2 - n) > 0.000001:
        if result ** 2 > n:
            hi = result
        else:
            lo = result
        result = (hi - lo) / 2 + lo
    return round(result, 6)

for i in range(101):
    print(f"square_root({i})={square_root(i)}")

i = 14856
print(f"square_root({i})={square_root(i)}")
