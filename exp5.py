print("NAME:manasviA UIN: 251A022")
print("DATE: 3-2-26")

l = []

NAME = []
AGE = []
SECTION = []

NAME_1 = input("ENTER YOUR NAME:")
NAME_2 = input("ENTER YOUR FREND'S NAME:")

AGE_1 = int(input("ENTER YOUR AGE:"))
AGE_2 = int(input("ENTER YOUR FREND AGE:"))

SECTION_1 = input("ENTER YOUR SECTION:")
SECTION_2 = input("ENTER YOUR FREND'S SECTION:")

l.append((NAME_1, AGE_1, SECTION_1))
l.append((NAME_2, AGE_2, SECTION_2))

print(l)
