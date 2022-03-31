#Program to change a given string to a new string where the first and last chars have been exchanged.

string=str(input("Enter a string :"))
first=string[0]                             #store first index element of string in variable
last=string[-1]                             #store last index element of string in variable

new=last+string[1:-1]+first                 #concatenate last the middle part and first part
print(new)

