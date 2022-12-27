'''
Let's continue on from the code above.

Create a guess.py program and type in the following:
'''

guess = 0
tries = 0

print("\t You have 5 tries to win this game, good luck!")

while guess != 6 and tries < 5:
    guess = int(input("Guess the number between 0 and 10: "))
    tries =tries + 1

if  guess != 6:
    print ("You lose no more tries remaining.")
else:
    print("You got it!")