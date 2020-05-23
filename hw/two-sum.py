#!/usr/bin/python3

def has2Sum(a, k):
    nums = set()
    for num in a:
        if k - num in nums: 
            return True;
        nums.add(num)
    return False



arr = [4,2,6,5,7,9,10]
print(has2Sum(arr, 13))
