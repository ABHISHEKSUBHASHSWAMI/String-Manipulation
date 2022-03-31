# Write a Python program to remove the characters which have odd index values of a given string

string=str(input("Enter a string :"))

new=""
for i in range (len(string)):
    if i%2==0:                                # add elements from index value which is divisible by 2 i.e even index
        new=new+string[i]

print(new)
