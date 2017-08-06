def createFibSeq(limit) : 
#    limit = input("enter the max value :")
    fibList = []
    fibList.append(1)
    fibList.append(2)
    fibListLength = len(fibList)-1
    newValue = 0
    while newValue <= limit:
        newValue = fibList[fibListLength] + fibList[fibListLength-1]
        if newValue < limit:
            fibList.append(newValue)
            fibListLength = fibListLength+1
        if newValue + fibList[fibListLength-1] > limit:
            break
        
    return fibList
        
        