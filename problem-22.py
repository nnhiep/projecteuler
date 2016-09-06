#!/usr/bin/env python3
import string


with open('./p022_names.txt') as f:
    s = f.read()
    # remove ""
    s = s.replace('"', '')
    lst = s.split(',')

    # sort alphabet
    lst.sort()

    ss = string.ascii_uppercase


def word_value(words):
    score = 0
    for c in words:
        score += ss.index(c) + 1
    return score

count = 0
for i in lst:
    count += word_value(i) * (lst.index(i) + 1)
print(count)
