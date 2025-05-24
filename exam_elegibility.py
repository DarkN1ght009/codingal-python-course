medical = input("Do u have a medical cause? If yes the put Y if no then put N : ")
attendance = int(input("Enter your attendence : "))
if medical == 'Y' :
    print ( "You are allowed for the exam")
else :
    if attendance >= 75 :
        print("You are allowed for the exam")
    else :
        print("You are not allowed for the exam")