import random

response = input("Press Y to roll the die ")
# if response == 'y' or 'Y':
#     no = random.randint(1,6)
# while not response == 'y' or 'Y':
#    response = input("Press Y to roll the die ")
response = 'y'

while response == 'y':
    no = random.randint(1,6)
    if no == 1:
        print("0-----")
    if no == 2:
        print("00----")
    if no == 3:
        print("000---")
    if no ==4:
        print("0000--")
    if no == 5:
        print("00000-")
    if no == 6:
        print("000000")
    response = input("Type y to roll again")
    print("\n")