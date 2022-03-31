#Program to calculate the length of a string

#smart way
string=str(input("Enter a string :"))
print(len(string))

#logical way
count=0                                        #initiate count=0
for i in string:                               #for each element in string
  count+=1                                     #count will increase by 1
print("length of the string is",count)
