math = float(input('Enter your maths marks :'))
english = float(input('Enter your english marks :'))
science = float(input('Enter your science marks :'))
hindi = float(input('Enter your hindi marks :'))

total = math + english + science + hindi

print ('THe total marks by combining all subjects is :',total)

percentage = (total / 400) * 100
print (" Your percentage is : ",percentage)