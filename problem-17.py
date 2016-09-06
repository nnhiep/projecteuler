#!/usr/bin/env python3

'''
For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

S = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]  # one, two
D = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]  # ten, twenty ...
H = 7  # hundred
T = 8  # thousand

# abcd
sum = 0
for i in range(1, 1000):
    c = i % 10  # singles digit
    b = int(((i % 100) - c) / 10)  # tens digit
    a = int(((i % 1000) - (b * 10) - c) / 100)  # hundreds digit

    if a != 0:
        sum += S[a] + H  # S[a] hundred
        if b != 0 or c != 0:
            sum += 3  # and
    if b == 0 or b == 1:
        sum += S[b * 10 + c]
    else:
        sum += D[b] + S[c]

sum += S[1] + T  # one thousand
print(sum)
