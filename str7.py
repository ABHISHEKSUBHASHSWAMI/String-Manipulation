#Program to count the character frequency in a string

string=input("Enter a String : ")
string=string.lower()                                     #convert string to lowercase

char=input("Enter a string calculate frequency :")
char=char.lower()                                         #conver character to lowercase

print(string.count(char))                                 #print occurance of character in string using count method
