#Function to insert a string in the middle of a string

def string_in():
    string=str(input("Enter a string :"))
    mid=len(string)//2
    word=str(input("Enter a word to insert in middle :"))

    new_string=string[:mid]+word+string[mid:]
    print(new_string)

string_in()
