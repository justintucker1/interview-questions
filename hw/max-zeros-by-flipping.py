#!/usr/bin/python3

def getMaxZeros(bits):
    l = r = zero_count = max_ones = 0
    while r < len(bits):
        if bits[r] == 0:
            zero_count += 1
            r += 1
            l = r
        else:
            max_ones = max(max_ones, r - l + 1)
            r += 1
    return zero_count + max_ones
    

bits1 = [0, 1, 0, 0, 1, 1, 0] # 6
bits2 = [0, 0, 0, 1, 0, 1] # 5
for bits in [bits1, bits2]:
    print(getMaxZeros(bits))
