#Program to change a given string to a new string where the first and last chars have been exchanged.

string=str(input("Enter a string :"))
first=string[0]
last=string[-1]

new=last+string[1:-1]+first
print(new)

