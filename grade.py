math = float(input("Enter your marks out of hundred in maths"))
hindi = float(input("Enter your marks out of hundred in hindi"))
english = float(input("Enter your marks out of hundred in english"))
science = float(input("Enter your marks out of hundred in science"))
ss = float(input("Enter your marks out of hundred in ss"))

total = math + hindi + english + science + ss
average = total / 5

if (average > 91 and average < 100) :
    print (" your grade is A1")
elif (average > 81 and average < 91) :
    print ("Your grade is A2")
elif (average > 71 and average < 81) :
    print ("Your grade is B1")
elif (average > 61 and average < 71) :
    print ("Your grade is B2")
elif (average > 51 and average < 61) :
    print ("Your grade is C1")
elif (average > 41 and average < 51) :
    print ("Your grade is C2")
else :
    print ("Invalid input")