#!/usr/bin/python3

# assume nums is a sorted rotated array of ints
# and nums has at least two values
def findSmallestNumber(nums):
    n = len(nums)
    if nums[0] <= nums[n - 1]: return 0
    if nums[n - 2] > nums[n - 1]: return n - 1
    if nums[0] > nums[1]: return 1

    lo, hi = 1, n - 2
    while lo <= hi:
        mid = (hi - lo) // 2 + lo
        if nums[mid - 1] > nums[mid]:
            return mid
        elif nums[lo] > nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    # should never get here
    return -1

def rotated_array_search(nums, target):
    if not nums: return false
    if len(nums) == 1: return nums[0] == target

    lo_index = findSmallestNumber(nums)
    if binary_search(nums, lo_index, len(nums) - 1, target):
        return True
    if binary_search(nums, 0, lo_index - 1, target):
        return True
    return False

def binary_search(nums, start, end, target):
    while start <= end:
        mid = (end - start) // 2 + start
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


# Examples:
# [35, 46, 79, 102, 1, 14, 29, 31], 46 --> True
# [35, 46, 79, 102, 1, 14, 29, 31], 47 --> False
# [35, 46, 79, 102, 1, 14, 29, 31], 47 --> false
# [7, 8, 9, 10, 1, 2, 3, 4, 5, 6], 9 --> true
# nums = [35, 46, 79, 102, 1, 14, 29, 31]
nums = [35, 46, 79, 102, 1, 14, 29, 31]
print(rotated_array_search(nums, 47))

