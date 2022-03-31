# Write a Python program to count the occurrences of each word in a given sentence.

string=str(input("Enter a string :"))
words=string.split()                                #store splitted string into variable
count=dict()                                        #initiate a dictionary

for word in words:                                  #initiate loop
    if(word in count):                              #if word is already in dictionary 
        count[word]=count[word]+1                   #increment the count
    else:                                           #else keep it 1
        count[word]=1
    
print(count)
