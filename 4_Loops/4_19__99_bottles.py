# String Interpolation

'''
String interpolation is a process of substituting values of variables into placeholders in a string.

For instance, if you have a template for saying hello to a person in an email like 'Hi {name}, nice to 
meet you!', you would like to replace the placeholder {name} with an actual name. This is string interpolation.
'''

# String Interpolation example - Number and square:
print("\tSquares")
for i in range(10):
    print(f"The square of {i} is {i*i}")

print("\n")

# 99 Bottles of Beer
'''
Create a 99_bottles.py program and use a for loop and a range() function to print out all the verses of 
"99 Bottles of Beer".
'''
print("\t99 Bottles of Beer")

for i in range(99, 0, -1):
    print(f"{i} bottles of beer on the wall")
    print(f"{i} bottles of beer")
    print(f"Take one down, pass it around")
    print(f"{i -1} bottles of beer on the wall")
