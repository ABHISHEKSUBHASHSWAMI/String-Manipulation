# Program that accepts a comma separated sequence of words as input and prints the unique words in sorted form

string=(input("Enter words separated by commas :"))
list=[]
for word in string.split(','):
    list=list+[sorted(word)]

print(list)
