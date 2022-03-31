#Program that, given a string that contains a decimal number,
#prints out the decimal part of the number. For instance, if given 5.74159, the program should print out .74159


string=str(input("Enter a decimal number :"))
new_string=string.split(".")
print("."+new_string[1])
