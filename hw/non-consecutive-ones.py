#!/usr/bin/python3

def getNonConsecOnes(n):
    ans = []
    def helper(s):
        if len(s) == n:
            ans.append(s)
            return
        helper(s + '0')
        if not s or s[-1] == '0':
            helper(s + '1')
    helper('')
    return ans

print(getNonConsecOnes(3))
            
