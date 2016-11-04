"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""


primes = [2]
cur = 3
goalPrimes = 10001
while len(primes) != goalPrimes:
    prime = True
    for p in primes:
        if cur % p == 0:
            prime = False
    if prime:
        primes.append(cur)
    cur += 1


print primes[len(primes)-1]
