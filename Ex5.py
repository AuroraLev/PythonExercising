#divisible by 5

import math

def listCreator(list):
    for i in range(0,5):
        print(f"Give the {i}st/snd/th number in the list: ")
        list.append(int(input()))

def fivediv(list):
    for i in range(len(list)):
        if list[i] % 5 == 0:
            print(list[i])
    return print("")
        
userlist = []

listCreator(userlist)

print(f"Given this list: {userlist}.")

print("These Numbers are divisble by 5: ")

print(fivediv(userlist))
