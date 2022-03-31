# Write a Python program to count the occurrences of each word in a given sentence.

string=str(input("Enter a string :"))
words=string.split()
count=dict()

for word in words:
    if(word in count):
        count[word]=count[word]+1
    else:
        count[word]=1
    
print(count)
