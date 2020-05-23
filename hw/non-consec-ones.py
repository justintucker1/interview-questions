#!/usr/bin/python3

def getNonConsecOnes(n):
    ans = []

    def f(s):
        if len(s) == n:
            ans.append(s)
            return
        f(s + '0')
        if not s or s[-1] != '1':
            f(s + '1')
    f('')       
    return ans

print(getNonConsecOnes(4))
