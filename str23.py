#Program that asks the user to enter a string. The program should then print the following:

#1 The total number of characters in the string
#2 The string repeated 10 times
#3 The first character of the string (remember that string indices start at 0)
#4 The first three characters of the string
#5 The last three characters of the string
#6 The string backwards
#7 The string with its first and last characters removed
#8 The string in all caps
#9 The string with every a replaced with an e
#10 The string with every letter replaced by a space

string=str(input("Enter a string :"))

#1
print(len(string))

#2
n=10
while(n>0):
    print(string)
    n-=1
    
#3
print("First character is :",string[0])

#4
print("First three characters are :",string[0:3])

#5
print("Last three characters are :",string[-3:])

#6
print("Backward string is :",string[::-1])

#7
print("First & last letter removed string :",string[1:-1])

#8
print("String in upper case is :",string.upper())

#9
print("Every a replaced by e in string :",string.replace("a","e"))

#10
print("Every letter in string replaced by space :"," "*len(string))
