#checks, if the first and the last number of a list are identical

def similiarLast(list):
    if list[0] == list[len(list)-1]:
        return print("Output True")
    else:
        return print("Output False")
   
userlist = []   
 
for i in range(0,4):
    userlist.append(int(input()))

print(userlist)

print(similiarLast(userlist))