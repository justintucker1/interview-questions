#!/usr/bin/python3

def getOnesCount(arr):

    def findLeftMostOnesIndex(arr): 
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if arr[mid] == 1:
                if mid == 0 or arr[mid - 1] == 0:
                    return mid
                else:
                    r = mid - 1
            else:
                l = mid + 1
        return -1

    index = findLeftMostOnesIndex(arr)
    return len(arr) - index if index >= 0 else 0
arr = [0,0,0,1,1,1,1,1,1,1,1]
print(getOnesCount(arr))
