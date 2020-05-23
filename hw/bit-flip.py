#!/usr/bin/python3

def bit_flip(bits, n):
    def f(F, B, C):
        if B == len(bits) or (F == 0 and bits[B] == 0):
            return C
        if bits[B] == 1:
            return f(F, B + 1, C + 1)
        else:
            on = f(F - 1, B + 1, C + 1)
            off = f(n, B + 1, 0)
            return max(on, off)
    return f(n, 0, 0)


bits = [0,1,1,1,0,1,0,1,0,0]
n = 2
#  Result:    7

print(bit_flip(bits, n))


