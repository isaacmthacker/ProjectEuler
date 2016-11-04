"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

#need improvement

import math

primes = [2]
below = 2000000
#below = 10
primeSum = 0
for x in range(3, below):
    if x % 100000 == 0:
        print x
    prime = True
    for p in primes:
        if x%p == 0:
            prime = False
            break
    if prime:
        primeSum += x
        primes.append(x)


print sum(primes)
