# Write a program in python to check if two strings are anagram or not.
# What is an anagram ?
# An anagram is word which is made using manipulating sequence of letters in another word.

str1=input("Enter first string :")              #get input for first string
str2=input("Enter second string :")             #get input for second string

if(sorted(str1)==sorted(str2)):                 #sort and compare each string
    print("These strings are anagram.")
else:
    print("These strings are not anagram.")

print(sorted(str1))
