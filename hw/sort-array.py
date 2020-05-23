#!/usr/bin/python3

def sortArray(a):
    i = j = 0
    while i < len(a) and j < len(a):
        if a[j] == 0:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1
    return a



arr = [0, 1, 1, 0, 1, 1, 1, 0]
print(sortArray(arr))
