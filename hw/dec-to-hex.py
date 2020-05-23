#!/usr/bin/python3

hex_nums = '0123456789abcdef'

def dec2hex(n):
    return (dec2hex(n // 16) if n > 15 else '') + hex_nums[n % 16] 

n = 16 ** 2 + 1
print(n,dec2hex(n))
