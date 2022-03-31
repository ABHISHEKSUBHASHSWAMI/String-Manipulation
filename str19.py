# Program to lowercase first n characters in a string

temp=str(input("Enter a string in upper case :"))
n=int(input("How many first characters do you want to in lower case:"))

new_string=temp[:n].lower()+temp[n:]

print(new_string)
