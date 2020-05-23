#!/usr/bin/python3

def print_reverse(a):
    def f(i):
        if i == len(a):
            return
        f(i + 1)
        print(a[i])
    f(0)

def reverse_string(str):
    def f(s):
        i = len(str) - len(s) - 1
        if i < 0:
            return s
        return f(s + str[i])
    return f('')

a = [1,2,3]
print_reverse(a)
print(reverse_string('hello'))

