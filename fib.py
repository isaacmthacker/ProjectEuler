"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms
"""




lst = [1,1]
idx = 1
for x in range(0,1000):
    newFib = lst[len(lst)-1] + lst[len(lst)-2]
    if newFib < 4000000:
        lst.append(newFib)
    else:
        print "no add"


total = 0
for fib in lst:
    if fib%2 == 0:
        total += fib
print total
