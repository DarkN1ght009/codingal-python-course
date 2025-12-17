print ('Hello I am an AI chat bot, What is your name?')

name = input()
print (f'Nice to meet you {name}.')

print ('How are you feeling today good/bad')
mood = input().lower()

if mood=='good' :
    print('I am glad to hear that')

elif mood=='bad' :
    print('I am sorry tohear that. I hope things get better soon')

else :
    print('I understand. It can be hard to express feelings at times.')

print (f'Goodbye{name}, it was nice meeting you')