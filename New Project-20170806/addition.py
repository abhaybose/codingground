def sumOfEvenNumbers(listOfNum) :
    
    listLength = len(listOfNum)
    sumOfEven = 0
    for i in range(listLength):
        if listOfNum[i]%2 ==0:
            sumOfEven = sumOfEven + listOfNum[i]
    
    
    return sumOfEven