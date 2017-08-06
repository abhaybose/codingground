import fibonnaci
import addition
instructions = """
All the operations are on Fibonnaci Sequence:

1. find the sum of all the even-valued terms. You need to provide teh limit of fobonnaci sequence [[Enter 1 to choose]]

Please enter your option 
"""
print instructions
choice = input("Enter you choice:")
if choice == 1 :
    limit = input("enter the max value :")
    varList =  fibonnaci.createFibSeq(limit)
    varSumOfEven = addition.sumOfEvenNumbers(varList)
    print "your fibonnaci sequence for the limit "+str(limit)+" is :"
    print varList
    print "varSumOfEven: "+str(varSumOfEven)
else:
    print "Invalid Choice"