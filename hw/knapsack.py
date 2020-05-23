#!/usr/bin/python3

'''
# recursion
def getMaxValue(weight_limit, weights, values):
    def f(W, V, depth):
        if W < 0: return -1
        if depth == len(weights): return V
        return max(
            f(W - weights[depth], V + values[depth], depth + 1), 
            f(W, V, depth + 1))
    return f(weight_limit, 0, 0)
'''

# iteration
def getMaxValue(weight_limit, weights, values):
    weight_count = weight_limit + 1
    item_count = len(weights) + 1
    V = [[0 for _ in range(weight_count)] for _ in range(item_count)]
    for i in range(1, item_count):
        for j in range(1, weight_count):
            off = V[i - 1][j]
            on = V[i - 1][j - weights[i - 1]] + values[i - 1] 
            V[i][j] = off if weights[i - 1] > j else max(on, off)
    return V[-1][-1]

weight_limit = 5
weights = [1, 3, 4, 2]
values = [3, 9, 12, 8]
print(getMaxValue(weight_limit, weights, values))
