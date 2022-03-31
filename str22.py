#Program to Sort Words in Alphabetic Order of a string

string="THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
new_string=[word.lower() for word in string.split()]
sorted_string=sorted(new_string)
for word in sorted_string:
    print(word, end=" ")
