# Control flow recap:
'''
- Control flow is the order in which the program's code executes.
- if statement tests a condition for truth and executes the code if it is True.
- elifclause can be added between if and else.
- else executes the code if none of the above is True.
- Relational operators are used to compare two values: ==, !=, >, >=, <, <=.

'''

# Final project of control flow unit

'''
The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides 
which of the four "Houses" each freshman student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin
Write a sortinghat.py program that asks the user some questions using int() and places them into one of 
the Houses based on their answers:
'''

# We create the variables for each house and set them to 0.
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

# Question 1
quest1 = int(input("Q1) Do you like Dawn or Dusk? \n   1) Dawn \n   2) Dusk \n"))

if quest1 == 1:
    Gryffindor = Gryffindor + 1
    Ravenclaw= Ravenclaw + 1
elif quest1 == 2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else:
    print("Choose one number from the options.")

# Question 2
quest2 = int(input("Q2) When I'm dead, I want people to member me as? \n   1) The Good \n   2) The Great \n   3) The Wise \n   4) The Bold \n   "))
if quest2 == 1:
    Hufflepuff = Hufflepuff + 1
elif quest2 == 2:
    Slytherin = Slytherin + 1
elif quest2 == 3:
    Ravenclaw= Ravenclaw + 1
elif quest2 == 4:
    Gryffindor = Gryffindor + 1
else:
    print("Remenber to choose one number from the options, muggle...")

# Question 3
quest3 = int(input("Q3) Which kind of instrument most pleases your ear? \n   1) The violin \n   2) The trumpet \n   3) The piano \n   4) The drum \n"))
if quest3 == 1:
    Slytherin = Slytherin + 1
elif quest3 == 2:
    Hufflepuff = Hufflepuff + 1
elif quest3 == 3:
    Ravenclaw= Ravenclaw + 1
elif quest3 == 4:
    Gryffindor = Gryffindor + 1
else:
    print("You don't belong to this school you filthy little mudblood")

# Question 4
quest4 = int(input("Q3) What is your favorite subject? \n   1) Charms \n   2) Potions \n   3) Astronomy \n   4) Defence Agains the Dark Arts \n   5) Herbology \n   6) History of Magic \n   7) Transfiguration \n"))
if quest4 == 1:
    Hufflepuff = Hufflepuff + 1
    Ravenclaw = Ravenclaw + 1
elif quest4 == 2:
    Slytherin = Slytherin + 1
    Gryffindor = Gryffindor + 1
elif quest4 == 3:
    Ravenclaw= Ravenclaw + 1
    Hufflepuff = Hufflepuff + 1
elif quest4 == 4:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif quest4 == 5:
    Hufflepuff = Hufflepuff + 1
elif quest4 == 6:
    Ravenclaw = Ravenclaw + 1
elif quest4 == 7:
    Gryffindor = Gryffindor + 1
    Slytherin = Slytherin + 1
else:
    print("Oh come ooon")

# Results and house show
result = print("You belong to: ")
if Gryffindor > Slytherin and Gryffindor > Hufflepuff and Gryffindor > Ravenclaw:
    print("\t🦁 Gryffindor!")
elif Ravenclaw > Slytherin and Ravenclaw > Hufflepuff and Ravenclaw > Gryffindor:
    print("\t🦅 Ravenclaw!")
elif Hufflepuff > Slytherin and Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw:
    print("\t🦡 Hufflepuff!")
elif Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw:
    print("\t🐍 Slytherin!")
else:
    print("You don't belong to this school you filthy little mudblood")

print("🦁: " + (str(Gryffindor)))
print("🦅: " + (str(Ravenclaw)))
print("🦡: "+ (str(Hufflepuff)))
print("🐍: " + (str(Slytherin)))
