# Program to Check Whether a String is Palindrome or Not.

string=str(input("Enter string to check :"))

if string==string[::-1]:
    print("It's Palindrome.")
else:
    print("It's not a palindrome.")
