#!/usr/bin/python3

'''
def getMaxSum(nums):
    max_sum, curr_sum = 0, 0
    for n in nums:
        curr_sum = max(curr_sum + n, n)
        max_sum = max(max_sum, curr_sum)
    return max_sum
        

def getMaxSum(nums):
    max_sum = 0

    def helper(curr_sum, index):
        if index == len(nums):
            return
        curr_max = max(nums[index], curr_sum + nums[index])
        nonlocal max_sum
        max_sum = max(max_sum, curr_max)
        helper(curr_max, index + 1)
        
    helper(0, 0)
    return max_sum

# jt 5/15/2020 
# try coming up with recursive algo
# based on idea that max is the bigger of an element
# or that same element plus the max of the array that
# preceeded that element
def getMaxSum(nums):

    # returns (global_max, local_max)
    def helper(arr):
        if not arr:
            return 0, 0
        global_max, helper_max = helper(arr[1:])
        local_max = max(helper_max + arr[0], arr[0])
        return max(global_max, local_max), local_max
    return helper(nums)[0]

'''

# jt 5/15
# discovered that kadane's is not really a DP problem
# could not find a clean formula for the recursive case
# The formula for max sum so far is what I had in mind
# but the answer is the max of all "best sums so far"
# in the recursion above I worked around this by returning
# a tuple with "global" and "local" maxes, where local
# is the value I need to use in the recursive function case
# and global is the actual max that I want to find
# Now - how to turn this into a tabular ("bottom-up")
# algorithm?
# Note that the basic resursive function is
# LOCAL_MAX(i) = max(LOCAL_MAX(i - 1) + VAL(i), VAL(i))
# and the base case is: if i == len -> 0
# and then you take the max of all LOCAL_MAXs
def getMaxSum(nums):
    local_max = global_max = 0
    for i in range(len(nums)):
        local_max = max(local_max + nums[i], nums[i])
        global_max = max(global_max, local_max)
    return global_max


# nums = [6, -1, 3, 5, -10]
nums = [-2, -3, 4, -1, -2, 1, 5, -3]
# nums = [1,2,3,-2,5]
# nums = [-1, -2, -3, -4]
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(getMaxSum(nums))
