#!/usr/bin/python3

'''
# O(2^n) time | O(n) space
def getMaxPalindromicLength(s):
  def f(l, r):
    if l == r: return 1
    if r - l == 1: return 2 if s[l] == s[r] else 1
    if s[l] == s[r]:
      return 2 + f(l + 1, r - 1)
    else: 
      return max(f(l + 1, r), f(l, r - 1))
  return f(0, len(s) - 1)     
'''  
# O(n^2) time | O(n^2) space
def getMaxPalindromicLength(s):
  n = len(s)
  m = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for l,r in zip(range(n), range(i,n)):
      if l == r:
        m[l][r] = 1
      elif r - l == 1:
        m[l][r] = 2 if s[l] == s[r] else 1
      elif s[l] == s[r]:
        m[l][r] = 2 + m[l + 1][r - 1]
      else:
        m[l][r] = max(m[l + 1][r], m[l][r - 1])    
  return m[0][-1]    
  
print(getMaxPalindromicLength('vtvvv'))  # 4
print(getMaxPalindromicLength('pwnnb'))  # 2
print(getMaxPalindromicLength('ttbtctcbt'))  # 7
