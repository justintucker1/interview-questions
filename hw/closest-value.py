#!/usr/bin/python3

def getClosestValue(arr, k): 
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (r - l) // 2 + l
        if arr[mid] == k:
            return k
        elif arr[mid] > k:
            r = mid - 1
        else:
            l = mid + 1
    lo = arr[r] if r >= 0 else arr[0]    
    hi = arr[l] if l < len(arr) else arr[len(arr) - 1]
    return lo if k - lo <= hi - k else hi

# [1, 2, 3, 5, 5, 7, 9, 10, 11], 6 --> 5
# [1, 2, 3], 8 --> 3
# [-2, -1, 0], -5 --> -2

# arr = [1, 2, 3, 5, 5, 7, 9, 10, 11]
# arr = [1, 2, 3]
arr = [-2, -1, 0]
print(getClosestValue(arr, -5))
