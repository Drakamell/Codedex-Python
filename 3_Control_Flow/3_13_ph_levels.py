'''
Relational operatos:
== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to

'''

ph = (int(input("Enter a pH value between 0 and 14: ")))
print(ph)

if ph > 7:
    print("Basic")
elif ph < 7:
    print("Acidic")
else:
    print("Neutral")