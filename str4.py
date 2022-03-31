#Write a program in python to find all duplicate characters in string.


string="Responsibility"                                 #take a string
original=[]                                             #creating a list to store string
duplicate=set()                                         #creating a set to store repeated string
for i in range (len(string)):                           #initiating a loop to traversing each string
    if string[i] in original:                           #condition- if string is already there in original list add it to set of duplicates
        duplicate.add(string[i])
    else:                                               #condition- else add it to original list
        original.append(string[i])

duplicate=list(duplicate)                               #convert set to list

for j in range(len(duplicate)):                         #print elements from the list
    print(",".join(duplicate[j]), end=" ")
