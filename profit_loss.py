cp = float(input("Enter your cost price : "))
sp = float(input("Enter your selling price : "))

if (cp<sp) :
    profit = sp - cp
    print ("Profit = ",profit)
elif (cp==sp) :
    print ('There is neither profit nor loss')
else :
    loss = cp - sp
    print ("Loss = ",loss)