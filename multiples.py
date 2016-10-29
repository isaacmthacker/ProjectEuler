num = 0
r = 1000
for x in range(1,r):
    if x%3 == 0 or x%5 == 0:
        num += x
print num
