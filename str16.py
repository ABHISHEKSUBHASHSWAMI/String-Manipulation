# Program to sort a string lexicographically


string=str(input("Enter a string :"))
string1=string.lower()
letters=sorted(list(string1))

for i in letters:
    print(i, end="")
