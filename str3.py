#Program in python to count and display vowels in a string.

string=str(input("Enter a string :"))                   #Take input string from user
vowels=list("AaEeIiOoUu")                               #Create a list containing vowels
check=[each for each in string if each in vowels]       #Create a list named check which will hold vowels from from string using advanced for loop

print(len(check))                                       #count of vowels
print(check)                                            #print vowels
