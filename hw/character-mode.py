#!/usr/bin/python3

# Examples
# 'hello' --> 'l'
# 'A walk in the park' --> 'a'
# 'noon' --> 'no'

def character_mode(string):
    freqs = [0 for _ in range(27)]
    max_letter_cnt = 0
    for c in string:
        if c.isalpha():
            index = ord(c.lower()) - ord('a')
            freqs[index] += 1
            max_letter_cnt = max(max_letter_cnt, freqs[index])
    ans = []
    for i in range(27):
        if freqs[i] == max_letter_cnt:
            ans.append(chr(i + ord('a')))
    return ''.join(ans)

print(character_mode('hello'))
