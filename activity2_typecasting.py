name = "penguin"
age = 15
is_student = True
weight = 38.5

print ('the type of your data is: ', type (name))
print ('the type of your data is: ', type (age))
print ('the type of your data is: ', type (is_student))
print ('the type of your data is: ', type (weight))

# type casting

print ('\n After typecasting .....')
age = str(age)
print(age)
print ('Data type of age is  :', type (age))
weight = int(weight)
print (weight)
print ('Data type of age is :', type(weight))