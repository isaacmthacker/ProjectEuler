



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










