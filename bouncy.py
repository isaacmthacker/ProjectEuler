"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""



def isBouncy(x):
    if len(x) >= 3:
        decreasing = True 
        increasing = True 
        same = True 
       
        for idx in range(1,len(x)):
            if x[idx-1] > x[idx]:
                decreasing = False
            if x[idx-1] < x[idx]:
                increasing = False
            if x[idx-1] != x[idx]:
                same = False

        if decreasing or increasing or same:
            #print (decreasing, increasing, same)
            return False


        return True

    else:
        return False


       
ratio = 0.0
goalRatio = 0.99
bouncy = 0
nonbouncy = 0
curNum = 1
while ratio != goalRatio:
    if isBouncy(str(curNum)):
        bouncy += 1
    else:
        nonbouncy += 1
    ratio = float(bouncy)/(nonbouncy+bouncy)
    curNum += 1

print curNum-1










