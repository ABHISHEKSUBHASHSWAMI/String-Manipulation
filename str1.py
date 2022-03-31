#Write a program to check if a Substring is Present in a Given String.

main_str=str(input("Enter a string :"))       #take the main string
sub_str=str(input("Enter a substring :"))     #take the substring

if (main_str.find(sub_str)==-1):
    print("NO")                               #find method returns -1 if no match found
else:
    print("YES")
