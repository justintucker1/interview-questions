#!/usr/bin/python3

def capPerms2(string):
    ans = set()
    n = len(string)
    for i in range(2**n, 2**(n+1)):
        mask = bin(i)[3:]
        ans.add(''.join(
            [string[j].lower() 
                if mask[j] == '0' or not string[j].isalpha() 
                else string[j].upper() 
                    for j in range(n)]))
    return list(reversed(sorted(ans)))

def capitalPerms(string):
    ans = []
    def helper(s, depth):
        if depth == len(string):
            ans.append(s)
            return
        helper(s + string[depth].lower(), depth + 1)
        if string[depth].isalpha():
            helper(s + string[depth].upper(), depth + 1)
    helper('', 0)         
    return ans

# Input: "A1d3"
# Output: ["A1D3", "a1D3", "A1d3", "a1d3"]
# s = "A1d3"
s = 'A1bC2'
print(capitalPerms(s))
print()
print()
print()
print(capPerms2(s))

