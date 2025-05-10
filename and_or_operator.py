num_1 = int(input ("Enter the first number : "))
num_2 = int(input ("Enter the second number : "))

if (num_1 > 0  and num_2 > 0 ) :
    print ("Both the numbers are positive and greadter than zero")
elif (num_1< 0 and num_1 < 0) :
    print ("Both the numbers are negative and less than zero ")
elif (num_1 == 0 or num_2 == 0) :
    print ("This is a special case ")
elif (num_1> 0 and num_2 < 0) :
    print ("Number 1 is positive while number 2 is negative")
else :
    print ('Number 1 is negative and number 2 is positive')
