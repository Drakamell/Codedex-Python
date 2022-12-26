import random

'''
Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.
'''

magic = random.randint(1,9)

question = input("Question: ")

magic_ball = print("Magic 8 Ball: ")
if magic == 1:
    print("Yes - definitely.")
elif magic == 2:
    print("It is decidedly so.")
elif magic == 3:
    print("Without a doubt.")
elif magic == 4:
    print("Reply hazy, try again.")
elif magic == 5:
    print("Ask again later.")
elif magic == 6:
    print("Better not tell you now.")
elif magic == 7:
    print("My sources say no.")
elif magic == 8:
    print("Outlook not so good.")
elif magic == 9:
    print("Very doubtful")