"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""





import math

for a in range(0,1000):
    for b in range(0,1000):
        c = math.sqrt(a*a + b*b)
        if a + b + c == 1000:
            if not (a == 0 or b == 0 or c == 0):
                print (a,b,c)
                print a*b*c

