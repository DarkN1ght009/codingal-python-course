amount = int(input("Enter the amount : "))

note_1 = amount // 2000
note_2 = (amount % 2000) // 500
note_3 = ((amount % 2000) % 500) // 100

print ('The number of 2000 notes = ',note_1)
print ('The number of 500 notes = ',note_2)
print ('The number of 100 notes = ',note_3)