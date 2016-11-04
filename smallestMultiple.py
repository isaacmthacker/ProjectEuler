"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def canDiv(x):
    for y in range(1,21):
        if x % y != 0:
            return False
    return True


cur = 20
while not canDiv(cur):
    cur += 20

print cur
