#!/usr/bin/python3

# log(m) + log(n) = log(mn)
# O(log(mn)) time | O(1) space
def findNumberInMatrix(matrix, target):
    lo, hi = 0, len(matrix) - 1 
    col = 0 
    while lo <= hi:
        mid = ((hi - lo) // 2) + lo
        val = matrix[mid][col]
        if val == target:
            return True
        if val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    row = lo - 1
    lo, hi = 0, len(matrix[0]) - 1
    while lo <= hi:
        mid = ((hi - lo) // 2) + lo
        val = matrix[row][mid]
        if val == target:
            return True
        if val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
    

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 3

targets = [-1, 0, 3, 50, 11, 12, 13, 51, 1]
for target in targets:
    print(findNumberInMatrix(matrix, target))
