"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def isPal(x):
    x = str(x)
    for i in range(1,len(x)):
        j = len(x)-1-i
        if x[i] != x[j]:
            return False
    return True


palindromes = []
for i in range(100,1000):
    for j in range(100,1000):
        ret = i*j
        if isPal(ret):
            palindromes.append(ret)

print max(palindromes)
