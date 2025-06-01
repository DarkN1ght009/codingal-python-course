string1 = str(input("Enter the word u want to reverse : "))

string2 = ('')

for i in string1 :
    string2 = i + string2


print ("\n The original string was : ", string1)
print ("Th new string is : ", string2)