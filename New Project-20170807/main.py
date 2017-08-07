print ("|Lets Find out the largest primary factor of the number you have in mind |:")
number = input("Enter your number(try a bigger one):")
print "The largest Primary Factor of "+str(number)+" is:"
prime = 2
pFactor = 0
while prime*prime < number:
    while number%prime ==0:
        number = number/prime
    pFactor = number
    prime = prime +1

print pFactor