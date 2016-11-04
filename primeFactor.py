"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def isPrime(x):
    for i in range(2,int(math.ceil(math.sqrt(x)))+1):
        if x % i == 0:
            return False
    return True

factors = []
check = 600851475143
x = int(math.ceil(math.sqrt(600851475143)))
for f in range(2, x+1):
    if check % f == 0:
        factors.append(f)

print factors
print [isPrime(x) for x in factors]



