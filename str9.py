#Write a Python program to remove the nthindex character from a nonempty str.

string=str(input("Enter a String :"))
value=int(input("Enter index number for character to be removed from string :"))

part1=string[:value]                                           #store sliced string till index value in part 1
part2=string[value+1:]                                         #store sliced string from index+1 to end in part 2
new_string=part1+part2                                         #concatenate part 1 and 2
print(new_string)
